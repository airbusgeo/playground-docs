import cv2
import geojson
import shapely.geometry
import numpy as np
from matplotlib import pyplot as plt
from .playground_objects import PlaygroundExport
from .utils import rasterize_feature_on_tile


class PlaygroundViewer(object):
    def __init__(self, job_name, input_dir, tags_to_label_dict,
                 labels_color_dict):
        """

        Args:
            job_name:
            input_dir:
            tags_to_label_dict:
        """
        print("Parsing Playground Export")
        self.playground_export = PlaygroundExport(job_name, input_dir)
        self.tags_to_labels_dict = tags_to_label_dict
        self.labels_color_dict = labels_color_dict
        self.tiles = [
            tile for dataset in self.playground_export.datasets
            for zone in dataset.zones for tile in zone.tiles
        ]
        print("Found {} datasets in {}/{}".format(
            len(self.playground_export.datasets), input_dir, job_name))
        print("Found {} zones in {}/{}".format(
            sum([
                len(dataset.zones)
                for dataset in self.playground_export.datasets
            ]), input_dir, job_name))
        print("Found {} tiles in {}/{}".format(
            len(self.tiles), input_dir, job_name))

        self.examples = []

    def check_random_tiles(self, nb_tiles_to_generate):
        """

        Args:
            nb_tiles_to_generate:

        Returns:

        """
        self.examples = []
        nb_unique_tiles = len(self.tiles)
        tiles_index = np.random.randint(
            nb_unique_tiles, size=nb_tiles_to_generate)

        for tile_index in tiles_index:
            self.images_from_tile(self.tiles[tile_index])
        self.plot_examples()

    def images_from_tile(self, tile):
        """

        Args:
            tile:

        Returns:

        """
        msk_path = tile.label_file
        with open(msk_path, "r") as f:
            feature_collection = geojson.load(f)

        data_mask = None
        features = []
        for feature in feature_collection['features']:
            if "mask" in feature['properties']:
                data_mask = shapely.geometry.shape(feature['geometry'])
            else:
                tags = feature['properties'].get('tags') or []
                kept_percentage = feature['properties'].get(
                    'kept_percentage') or 1.0
                labels = []
                if not isinstance(tags, list):
                    tags = [tags]
                for tag in tags:
                    labels.append(self.tags_to_labels_dict.get(tag) or None)
                labels = list(
                    set([label for label in labels if label is not None]))
                for label in labels:
                    features.append(
                        geojson.Feature(
                            geometry=feature['geometry'],
                            properties={
                                "label": label,
                                "kept_percentage": kept_percentage
                            }))
        example = []
        assert len(tile.sample_files) > 0
        for sample_file in tile.sample_files:
            img = cv2.imread(sample_file, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            example.append(img)

        h, w = example[0].shape[:2]

        gt = np.zeros((h, w, 3), dtype=np.uint8)
        no_data_mask = shapely.geometry.box(0, 0, h, w)
        no_data_mask = no_data_mask.difference(data_mask)
        gt = rasterize_feature_on_tile(
            gt, no_data_mask, color=(128, 128, 128))
        for feature in features:
            polygon = shapely.geometry.shape(feature['geometry'])
            label = feature['properties']['label']
            gt = rasterize_feature_on_tile(
                gt, polygon, color=self.labels_color_dict[label])

        example.append(gt)
        self.examples.append(example)

    def plot_examples(self):
        """

        Returns:

        """
        fig, axarr = plt.subplots(
            len(self.examples), len(self.examples[0]), figsize=(20, 40))
        for i, example in enumerate(self.examples):
            for k, img in enumerate(example):
                axarr[i, k].imshow(img)
        plt.show()
