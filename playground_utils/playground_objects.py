import os
import glob
import json
import tqdm


class PlaygroundExport(object):
    def __init__(self, export_dir, job_name):
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
        self.input_dir = export_dir
        self.job_name = job_name
        self.datasets = []

        assert os.path.exists(os.path.join(
            export_dir,
            job_name + ".json")), "No json files found in {}".format(
                os.path.join(export_dir, job_name + ".json"))
        with open(os.path.join(export_dir, job_name + ".json"), "r") as f:
            config = json.loads(f.read())
            self.zoom = config.get("targetZoom")
            self.datasets_ids = config.get("datasetIds")

            for dataset_id in tqdm.tqdm(
                    self.datasets_ids, desc="Findind dataset files"):
                self.datasets.append(PlaygroundDataset(export_dir, dataset_id))

    def __repr__(self):
        s = " {} - {}\n".format(self.input_dir, self.job_name)
        s += " {} Zones {} Tiles\n".format(
            sum([len(dataset.zones) for dataset in self.datasets]),
            sum([
                len(zone.tiles) for dataset in self.datasets
                for zone in dataset.zones
            ]),
        )
        for dataset in self.datasets:
            s += "Dataset {}: {} zones - {} tiles\n".format(
                dataset.dataset_id, len(dataset.zones),
                sum([len(zone.tiles) for zone in dataset.zones]))

        return s


class PlaygroundDataset(object):
    def __init__(self, export_dir, dataset_id):
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
                    PlaygroundZone(export_dir, dataset_id, zone_id, image_ids))


class PlaygroundZone(object):
    def __init__(self, export_dir, dataset_id, zone_id, image_ids):
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
        self.export_dir = export_dir
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
        tile_id = os.path.splitext(os.path.basename(label_file))[0]

        tile = PlaygroundTile(self.export_dir, self.dataset_id, self.zone_id,
                              self.image_ids, tile_id)

        if tile.sample_files is not None:
            return tile
        else:
            return None


class PlaygroundTile(object):
    def __init__(self, export_dir, dataset_id, zone_id, image_ids, tile_id):
        """

        Args:
            dataset_id:
            zone_id:
            label_file:
            sample_files:
        """
        self.export_dir = export_dir
        self.dataset_id = dataset_id
        self.zone_id = zone_id
        self.image_ids = image_ids
        self.tile_id = tile_id

        self.target_file = os.path.join(self.export_dir, self.dataset_id,
                                        "labels", self.zone_id,
                                        tile_id + ".json")
        self.sample_files = []

        self._find()

    def _find(self):
        samples_dirs = [
            os.path.join(self.export_dir, self.dataset_id, "samples",
                         self.zone_id, image_id) for image_id in self.image_ids
        ]

        sample_files = []
        for sample_dir in samples_dirs:
            if os.path.exists(os.path.join(sample_dir, self.tile_id + ".jpg")):
                sample_files.append(
                    os.path.join(sample_dir, self.tile_id + ".jpg"))
            elif os.path.exists(
                    os.path.join(sample_dir, self.tile_id + ".png")):
                sample_files.append(
                    os.path.join(sample_dir, self.tile_id + ".png"))

        if len(sample_files) == len(samples_dirs):
            self.sample_files = sample_files
        else:
            self.sample_files = None
