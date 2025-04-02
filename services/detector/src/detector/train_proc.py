
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
    logs: Queue,
):

    def on_train_epoch_end(trainer):
        """
        Custom callback executed at the end of each training epoch.

        Args:
            trainer: The YOLO Trainer object.
        """
        epoch = trainer.epoch  # Current epoch number
        results = trainer.metrics  # Training metrics (loss, mAP, etc.)

        updates.put(epoch)
        # Example: Log the loss
        if results:
            pass
            # print(results)
            # print(f"Loss: {results.box.loss:.4f}, "
            #    f"Label Loss: {results.cls.loss:.4f}, "
            #    f"Object Loss: {results.dfl.loss:.4f}"

            # training_session.box_loss = results['box']['loss']
            # training_session.class_loss = results['cls']['loss']
            # training_session.object_loss = results['dfl']['loss']

        # updates.put([session,training_session])

        # asyncio.create_task(self.api.updateSession(session, training_session))

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