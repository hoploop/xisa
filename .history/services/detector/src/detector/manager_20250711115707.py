# PYTHON IMPORTS
import asyncio
from io import BytesIO
import logging
import os
from multiprocessing import Queue
import shutil
import threading
from typing import Optional
from ultralytics import YOLO
import yaml

# LIBRARY IMPORTS
from PIL import Image

# LOCAL IMPORTS
from common.clients.api import ApiClient
from common.clients.storage import StorageClient
from common.clients.trainer import TrainerClient
from common.models.auth import User
from common.models.detector import Detector, DetectorImage, DetectorImageLabel, DetectorImageMode, DetectorLabel, DetectorTrainingSession
from common.models.trainer import TrainSessionStatus
from detector.config import DetectorServiceConfig


#INITIALIZATION
log = logging.getLogger(__name__)

class DetectorManager:
    
    def __init__(self,config:DetectorServiceConfig,detector: Detector,storage:StorageClient,trainer:TrainerClient,api:ApiClient):
        self.config: DetectorServiceConfig = config
        self.detector: Detector = detector
        self.storage: StorageClient = storage
        self.trainer: TrainerClient = trainer
        self.api: ApiClient = api
        
    async def setup(self,session:str):
        log.debug("Create detector paths")
        await self.progress(session,100,3,"Creating detector folders")
        
        # This is the target model.pt path: e.g. data/detectors/{id}/model.pt
        target_model_path = os.path.join(self.config.path, str(self.detector.id), self.config.name)
        
        # This is the folder name: e.g. data/detectors/{id}
        folder_name = os.path.join(self.config.path, str(self.detector.id))

        # If detector_folder exists, reset it
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            log.debug("Removing legacy detector folder: {0}".format(folder_name))
            shutil.rmtree(folder_name)

        # Create the folder: e.g. data/detectors/{id}
        log.debug("Create detector folder: {0}".format(folder_name))
        os.mkdir(folder_name)

        # Create the labels folder: e.g. data/detectors/{id}/labels
        labels_path = os.path.join(folder_name, "labels")
        log.debug("Create labels folder: {0}".format(labels_path))
        os.mkdir(labels_path)
            
        # Create the labels train folder: e.g. data/detectors/{id}/labels/train
        labels_train_path = os.path.join(labels_path, "train")
        log.debug("Create labels train folder: {0}".format(labels_train_path))
        os.mkdir(labels_train_path)
        
        # Create the labels val folder: e.g. data/detectors/{id}/labels/val
        labels_val_path = os.path.join(labels_path, "val")
        log.debug("Create labels val folder: {0}".format(labels_val_path))
        os.mkdir(labels_val_path)

        # Create the labels test folder: e.g. data/detectors/{id}/labels/test
        labels_test_path = os.path.join(labels_path, "test")
        log.debug("Create labels test folder: {0}".format(labels_test_path))
        os.mkdir(labels_test_path)

        # Create the images folder: e.g. data/detectors/{id}/images
        images_path = os.path.join(folder_name, "images")
        log.debug("Create images folder: {0}".format(images_path))
        os.mkdir(images_path)

        # Create the images train folder: e.g. data/detectors/{id}/images/train
        train_path = os.path.join(images_path, "train")
        log.debug("Create images train folder: {0}".format(train_path))
        os.mkdir(train_path)

        # Create the images test folder: e.g. data/detectors/{id}/images/test
        test_path = os.path.join(images_path, "test")
        log.debug("Create images test folder: {0}".format(test_path))
        os.mkdir(test_path)

        # Create the images val folder: e.g. data/detectors/{id}/images/val
        val_path = os.path.join(images_path, "val")
        log.debug("Create images val folder: {0}".format(val_path))
        os.mkdir(val_path)

        # The original model path: e.g. data/detectors/yolo11n.pt
        original_model_path = os.path.join(self.config.path, self.config.original)
        
        # The original classes path: e.g. data/detectors/classes.yaml
        original_classes_filename = os.path.join(self.config.path, self.config.classes)
        
        
        log.debug("Copy detector model: {0} -> {1}".format(original_model_path,target_model_path))
        shutil.copyfile(original_model_path, target_model_path)
        
        await self.progress(session,100,10,"Creating class files")
        log.debug("Loading original classes: {0}".format(original_classes_filename))
        with open(original_classes_filename, "r") as classes_file:
            classes = yaml.load(classes_file,Loader=yaml.Loader)
            for class_name_id in classes["names"]:
                class_name = classes["names"][class_name_id]
                log.info("Creating class for: '{0}'".format(class_name))
                found_label = await DetectorLabel.find(
                    DetectorLabel.detector == self.detector.id,
                    DetectorLabel.name == class_name,
                ).first_or_none()
                if not found_label:
                    await DetectorLabel(
                        name=class_name, detector=self.detector.id
                    ).insert()

        log.debug("Create model configuration")
        config_data = dict(
            path=os.path.join(os.getcwd(), self.config.path, str(self.detector.id))
            + "/",
            train="images/train",
            val="images/val",
            test="images/test",
            nc=classes["nc"],
            names=classes["names"],
        )
        
        
        log.debug("Loading detector labels")
        await self.progress(session,100,20,"Loading detector labels")
        labels = await DetectorLabel.find(DetectorLabel.detector == self.detector.id).to_list()

        log.debug("Updating class names")
        class_by_number = {}
        class_by_name = {}
        for label in labels:
            if label.name not in list(config_data["names"].values()):
                n = str(len(list(config_data["names"].keys())))
                config_data["names"][int(n)] = label.name
        for key in config_data["names"].keys():
            class_by_number[key] = config_data["names"][key]
            class_by_name[config_data["names"][key]] = key

        config_data["nc"] = len(list(config_data["names"].keys()))

        
        # Yaml filename: e.g. data/detectors/{id}/data.yaml
        await self.progress(session,100,25,"Updating detector configuration")
        config_filename = os.path.join(self.config.path, str(self.detector.id), self.config.data)
       
        log.debug("Saving model configuration: {0}".format(config_filename))
        with open(config_filename, "w") as outfile:
            yaml.dump(config_data, outfile, default_flow_style=False)
       
       
        log.debug("Loading detector images")
        await self.progress(session,100,30,"Loading detector images")
        images_count = await DetectorImage.find(DetectorImage.detector == self.detector.id).count()
        images = await DetectorImage.find(DetectorImage.detector == self.detector.id).to_list()
        log.debug("Identified {0} detector images".format(images_count))
        
        for image in images:
            if not image.storage: continue
            log.debug("Loading image: {0}".format(str(image.storage)))
            data, content_type, size = await self.storage.loadById(image.storage)
            img = Image.open(BytesIO(data))
            width, height = img.size
            
            sub_path = ""
            if image.mode == DetectorImageMode.train:
                sub_path = "train"
            elif image.mode == DetectorImageMode.val:
                sub_path = "val"
            else:
                sub_path = "test"
                
            suffix_name = str(image.id) + ".png"
            if image.mode == DetectorImageMode.train:
                image_filename = os.path.join(train_path, suffix_name)
            elif image.mode == DetectorImageMode.test:
                image_filename = os.path.join(test_path, suffix_name)
            else:
                image_filename = os.path.join(val_path, suffix_name)

            log.debug("Saving image: {0}".format(image_filename))
            img.save(image_filename, quality=100, subsampling=0)

            image_box_file = os.path.join(
                os.getcwd(),
                self.config.path,
                str(self.detector.id),
                "labels",
                sub_path,
                str(image.id) + ".txt",
            )
            log.debug("Create image boxes: {0}".format(image_box_file))
            lines = []
            image_labels = await DetectorImageLabel.find(DetectorImageLabel.image == image.id).to_list()
            for image_label in image_labels:
                dlabel = await DetectorLabel.find_many(
                    DetectorLabel.id == image_label.label
                ).first_or_none()
                if dlabel:
                    label_name = dlabel.name
                    w = (image_label.xend - image_label.xstart) / image.width
                    h = (image_label.yend - image_label.ystart) / image.height
                    x = image_label.xend / image.width - (w / 2)
                    y = image_label.yend / image.height - (h / 2)

                    # 16 0.048093 0.081250 0.051410 0.064583
                    line = "{0} {1:0.6f} {2:0.6f} {3:0.6f} {4:0.6f} ".format(
                        class_by_name[label_name], x, y, w, h
                    )
                    log.debug(line)
                    lines.append(line)
                    
            log.debug("Updating image box file: {0}".format(image_box_file))
            with open(image_box_file, "w") as f:
                f.writelines(line + "\n" for line in lines)

        # Failover for no val images
        await self.progress(session,100,40,"Loading no val images")
        val_images_number = len(
            [
                name
                for name in os.listdir(val_path)
                if os.path.isfile(os.path.join(val_path, name))
            ]
        )
        if val_images_number == 0:
            for fname in os.listdir(train_path):
                # copying the files to the
                # destination directory
                shutil.copy2(os.path.join(train_path, fname), val_path)
                
        await self.progress(session,100,50,"Initial folder setup completed")


    async def progress(self,session:str,total:int,value:int,message:Optional[str]=None):
        dts = DetectorTrainingSession(detector=self.detector.id,total=total,progress=value,message=message)
        await self.api.updateSession(session, dts)
        
    async def updateProgress(self,session:str,results:Queue,progresses:Queue):
        while results.empty():
            if not progresses.empty():
                progr = progresses.get()
                await self.progress(session,progr[0],progr[1],progr[2])
            await asyncio.sleep(0.5)
            
        save_dir = results.get()

        log.debug("Results are saved into: {0}".format(save_dir))
        self.detector.best = os.path.join(save_dir, "weights/best.pt")
        self.detector.last = os.path.join(save_dir, "weights/last.pt")
        training_session.epoch_progress = epochs
        await self.progress(session,100,100,"Training completed")

        await self.trainer.trainSessionUpdate(
            user, trainSessionId, TrainSessionStatus.COMPLETED, results=str(save_dir)
        )

        await self.detector.save()
        
        

    async def train(self,epochs:int,user:User,session:str,image_size:int):
        log.debug("Starting detector {0} training session, for {1} epochs and image size {2}".format(self.detector.name,epochs,image_size))
        await self.progress(session,100,1,"Setting up detector filesystem")
        await self.setup(session)
        
        await self.progress(session,100,51,"Starting the new training")
        
        trainSessionId = None
        try:

            results = Queue()
            progresses = Queue()
            
            trainSessionId = await self.trainer.trainSessionCreate(user, self.detector.id)
            await self.trainer.trainSessionUpdate(
                user, trainSessionId, TrainSessionStatus.RUNNING
            )

            path = os.path.join(self.config.path, str(self.detector.id), self.config.name)
            if not os.path.exists(path):
                raise Exception("detector.errors.not_found")
                

            asyncio.create_task(
                self.updateProgress(
                    session,
                    results,
                    progresses,
                )
            )

            thread = threading.Thread(
                target=self.trainYOLO,
                args=(
                    path,
                    image_size,
                    epochs,
                    results,
                    errors,
                ),
                daemon=True,
            )
            thread.start()

            return True
        except Exception as e:
            log.warning(str(e))
            if trainSessionId:
                await self.trainer.trainSessionUpdate(
                    user, trainSessionId, TrainSessionStatus.ERROR, error=str(e)
                )

            return False


    def trainYOLO(
        self,
        path: str,
        image_size: int,
        epochs: int,
        results: Queue,
        progresses: Queue,
        errors: Queue,
    ):

        def on_train_epoch_end(trainer):
            """
            Custom callback executed at the end of each training epoch.

            Args:
                trainer: The YOLO Trainer object.
            """
            epoch = trainer.epoch  # Current epoch number
            metrics = trainer.metrics  # Training metrics (loss, mAP, etc.)
            keys,vals = list(metrics.keys()), list(metrics.values())
            #print("Values:", vals)
            #print("Keys:",keys)
            #epoch: epochs = x: 40
            x = round(epoch * 40 / epochs)
            updates.put(epoch)
            
        try:

            # Load a COCO-pretrained YOLO11n model
            progresses.put((100,52,"Loading YOLO Model"))
            model = YOLO(path)

            # Train the model on the COCO8 example dataset for 100 epochs
            progresses.put((100,53,"Train the model on the COCO8 example dataset for 100 epochs"))
            data_path = os.path.join(self.config.path, str(self.detector.id), self.config.data)
            runs_path = os.path.join(self.config.path, str(self.detector.id), self.config.runs)

            ### TRAINING CORE
            model.add_callback("on_train_epoch_end", on_train_epoch_end)
            progresses.put((100,59,"Starting the training"))
            train_results = model.train(
                data=data_path, epochs=epochs, imgsz=image_size, project=runs_path
            )
            ## END TRAINING CORE
            
            results.put(train_results.save_dir)
        except Exception as e:
            log.warning(str(e))
            errors.put(str(e))