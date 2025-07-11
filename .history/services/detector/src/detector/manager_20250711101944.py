# PYTHON IMPORTS
import logging
import os

# LOCAL IMPORTS
from common.models.detector import Detector, DetectorImage, DetectorLabel
from detector.config import DetectorServiceConfig


#INITIALIZATION
log = logging.getLogger(__name__)

class DetectorManager:
    
    def __init__(self,config:DetectorServiceConfig,detector: Detector):
        self.config: DetectorServiceConfig = config
        self.detector: Detector = detector
        
    async def setup_folder(self):
        labels = await DetectorLabel.find(DetectorLabel.detector == self.detector.id).to_list()
        images = await DetectorImage.find(DetectorImage.detector == self.detector.id).to_list()

        yaml_filename = os.path.join(self.config.path, str(self.detector.id), self.config.data)
        with open(yaml_filename, "r") as infile:
            yaml_file = yaml.load(infile,Loader=yaml.Loader)

        class_by_number = {}
        class_by_name = {}
        for label in labels:
            if label.name not in list(yaml_file["names"].values()):
                n = str(len(list(yaml_file["names"].keys())))
                yaml_file["names"][int(n)] = label.name
        for key in yaml_file["names"].keys():
            class_by_number[key] = yaml_file["names"][key]
            class_by_name[yaml_file["names"][key]] = key

        yaml_file["nc"] = len(list(yaml_file["names"].keys()))

        with open(yaml_filename, "w") as outfile:
            yaml.dump(yaml_file, outfile)

        for image in images:
            image_labels = await DetectorImageLabel.find(
                DetectorImageLabel.image == image.id
            ).to_list()

            sub_path = ""
            if image.mode == DetectorImageMode.train:
                sub_path = "train"
            elif image.mode == DetectorImageMode.val:
                sub_path = "val"
            else:
                sub_path = "test"

            image_box_file = os.path.join(
                os.getcwd(),
                self.config.path,
                str(detector_id),
                "labels",
                sub_path,
                str(image.id) + ".txt",
            )
            lines = []
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
            with open(image_box_file, "w") as f:
                f.writelines(line + "\n" for line in lines)

        # Failover for no val images
        image_path = os.path.join(
            os.getcwd(), self.config.path, str(detector_id), "images"
        )
        image_train_path = os.path.join(image_path, "train")
        image_val_path = os.path.join(image_path, "val")
        image_test_path = os.path.join(image_path, "test")
        val_images_number = len(
            [
                name
                for name in os.listdir(image_val_path)
                if os.path.isfile(os.path.join(image_val_path, name))
            ]
        )
        if val_images_number == 0:
            for fname in os.listdir(image_train_path):

                # copying the files to the
                # destination directory
                shutil.copy2(os.path.join(image_train_path, fname), image_val_path)
