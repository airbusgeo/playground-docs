import os
import glob
import json


class PlaygroundExport(object):
    def __init__(self, job_name, export_dir):
        """
        An Export class that is the main class and contains Datasets
        Initializing a PlaygroundExport Class will automatically find all datasets inside this export 
        
        Attributes:
        dataset_ids: list of dataset_ids in this export job
        datasets: list of PlaygroundDataset objects
        zoom: Zoom at which data was exported
        Args:
            job_name: The job name (usually the dir name)
            export_dir: The path to the export directory (should point to /data/job-name/)
        """
        self.job_name = job_name
        self.input_dir = export_dir

        assert os.path.exists(os.path.join(
            export_dir,
            job_name + ".json")), "No json files found in {}".format(
                os.path.join(export_dir, job_name + ".json"))
        with open(os.path.join(export_dir, job_name + ".json"), "r") as f:
            config = json.loads(f.read())
            self.zoom = config.get("targetZoom")
            self.datasets_ids = config.get("datasetIds")
            self.datasets = []
            for dataset_id in self.datasets_ids:
                export_dir = os.path.join(export_dir)
                self.datasets.append(PlaygroundDataset(dataset_id, export_dir))


class PlaygroundDataset(object):
    def __init__(self, dataset_id, export_dir):
        """
        The Playground Dataset Export class that contains zones
        Automatically created by PlaygroundExport class
        Args:
            dataset_id: The dataset id 
            export_dir:  The path to the export directory (should point to /data/job-name/ where the dataset dir is /data/job-name/dataset-id) 
        """
        self.dataset_id = dataset_id
        self.dataset_dir = os.path.join(export_dir, dataset_id)

        assert os.path.exists(
            os.path.join(
                self.dataset_dir,
                dataset_id + ".json")), "No json files found in {}".format(
                    os.path.join(self.dataset_dir, dataset_id + ".json"))
        with open(os.path.join(self.dataset_dir, dataset_id + ".json"),
                  "r") as f:
            config = json.loads(f.read())
            self.zone_ids = config.get("zoneIds")
            self.image_ids = config.get("imageIds")

            self.zones = []

            for i, zone_id in enumerate(self.zone_ids):
                image_ids = self.image_ids[i]
                if not isinstance(image_ids, list):
                    image_ids = [image_ids]
                self.zones.append(
                    PlaygroundZone(dataset_id, zone_id, image_ids, export_dir))


class PlaygroundZone(object):
    def __init__(self, dataset_id, zone_id, image_ids, export_dir):
        """
        A Playground Zone (that contain tiles objects). Automatically created by the Dataset class
        A zone is a list of WMTS tiles belonging to a certain undisclosed geographical location.
        A zone can cover one or several image_ids depending on the export type (object detection or change detection)
        On init, this objects automatically find 

        Args:
            dataset_id: Parent dataset id
            zone_id: This zone id (the path to this zone is /data/job-name/dataset_id/zone_id)
            image_ids: Image_ids where this zone is located
            export_dir:
        """
        self.dataset_id = dataset_id
        self.zone_id = zone_id
        self.image_ids = image_ids
        self.labels_dir = os.path.join(export_dir, dataset_id, "labels",
                                       zone_id)
        self.samples_dirs = [
            os.path.join(export_dir, dataset_id, "samples", zone_id, image_id)
            for image_id in image_ids
        ]

        label_files = glob.glob(os.path.join(self.labels_dir, "*.json"))

        self.tiles = map(self.find_tiles, label_files)
        self.tiles = [tile for tile in self.tiles if tile is not None]

    def find_tiles(self, label_file):
        """

        Args:
            label_file:

        Returns:

        """
        label_id = os.path.splitext(os.path.basename(label_file))[0]
        sample_files = []
        for sample_dir in self.samples_dirs:
            if os.path.exists(os.path.join(sample_dir, label_id + ".jpg")):
                sample_files.append(
                    os.path.join(sample_dir, label_id + ".jpg"))
            elif os.path.exists(os.path.join(sample_dir, label_id + ".png")):
                sample_files.append(
                    os.path.join(sample_dir, label_id + ".png"))
        if len(sample_files) == len(self.samples_dirs):
            return PlaygroundTile(self.dataset_id, self.zone_id, label_file,
                                  sample_files)
        else:
            return None


class PlaygroundTile(object):
    def __init__(self, dataset_id, zone_id, label_file, sample_files):
        """

        Args:
            dataset_id:
            zone_id:
            label_file:
            sample_files:
        """
        self.dataset_id = dataset_id
        self.zone_id = zone_id
        self.tile_id = os.path.splitext(os.path.basename(label_file))[0]
        self.label_file = label_file
        self.sample_files = sample_files
