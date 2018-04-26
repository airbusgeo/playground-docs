import cv2
import numpy as np

def rasterize_feature_on_tile(tile, polygon, color=(0, 255, 0), mode="fill"):
    img_mask = np.zeros_like(tile)
    if not polygon:
        return tile

    def int_coords(x):
        return np.array(x).round().astype(np.int32)

    exteriors = [int_coords(polygon.exterior.coords)]
    interiors = [int_coords(pi.coords) for pi in polygon.interiors]
    if mode is not "fill":
        cv2.polylines(img_mask, exteriors, 1, (1, 1, 1))
    else:
        cv2.fillPoly(img_mask, exteriors, (1, 1, 1))
        cv2.fillPoly(img_mask, interiors, (0, 0, 0))
    tile[np.all(img_mask != np.asarray((0, 0, 0)), axis=-1), :] = color
    return tile