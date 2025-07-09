
import os
from ultralytics import YOLO
from multiprocessing import Queue


def trainYOLO(
    detector_id: str,
    config_path: str,
    config_data: str,
    config_runs: str,
    path: str,
    image_size: int,
    epochs: int,
    updates: Queue,
    results: Queue,
    errors: Queue,
    logs: Queue,
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

        updates.put(epoch)
        
    try:

        # Load a COCO-pretrained YOLO11n model
        logs.put("Loading YOLO Model")
        model = YOLO(path)

        # Train the model on the COCO8 example dataset for 100 epochs
        logs.put("Train the model on the COCO8 example dataset for 100 epochs")
        data_path = os.path.join(config_path, str(detector_id), config_data)
        runs_path = os.path.join(config_path, str(detector_id), config_runs)

        ### TRAINING CORE
        model.add_callback("on_train_epoch_end", on_train_epoch_end)
        logs.put("Starting the training")
        train_results = model.train(
            data=data_path, epochs=epochs, imgsz=image_size, project=runs_path
        )
        logs.put("Ending the training")
        ## END TRAINING CORE

        updates.put(epochs)
        results.put(train_results.save_dir)
    except Exception as e:
        errors.put(str(e))