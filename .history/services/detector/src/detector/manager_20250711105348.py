# PYTHON IMPORTS
from io import BytesIO
import logging
import os
import shutil

import yaml

# LIBRARY IMPORTS
from PIL import Image

# LOCAL IMPORTS
from common.clients.storage import StorageClient
from common.models.detector import Detector, DetectorImage, DetectorImageLabel, DetectorImageMode, DetectorLabel
from detector.config import DetectorServiceConfig


#INITIALIZATION
log = logging.getLogger(__name__)

class DetectorManager:
    
    def __init__(self,config:DetectorServiceConfig,detector: Detector,storage:StorageClient):
        self.config: DetectorServiceConfig = config
        self.detector: Detector = detector
        self.storage: StorageClient = storage
        
    async def setup_folder(self):
        log.debug("Create detector paths")
        
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
        config_filename = os.path.join(self.config.path, str(self.detector.id), self.config.data)
       
        log.debug("Saving model configuration: {0}".format(config_filename))
        with open(config_filename, "w") as outfile:
            yaml.dump(config_data, outfile, default_flow_style=False)
       
       
        log.debug("Loading detector images")
        images_count = await DetectorImage.find(DetectorImage.detector == self.detector.id).count()
        images = await DetectorImage.find(DetectorImage.detector == self.detector.id).to_list()
        log.debug("Identified {0} detector images".format(images_count))
        
        for image in images:
            
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


    