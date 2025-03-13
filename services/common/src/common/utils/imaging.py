
# PYTHON IMPORTS
from itertools import combinations

# LIBRARY IMPORTS

import numpy as np

class ImageGrid:

    def __init__(self, img_width, img_height):
        self.img_width = img_width
        self.img_height = img_height

    def classify_box(self, rows, cols, x, y, width, height):
        """Classify a box into a row and column using its center point."""
        cell_width = self.img_width / cols
        cell_height = self.img_height / rows

        center_x = x + width / 2
        center_y = y + height / 2

        col = int(center_x / cell_width)
        row = int(center_y / cell_height)

        return row, col

    def compute_overlap(box1, box2):
        """Check if two boxes overlap and return the overlap area."""
        x1, y1, w1, h1 = box1
        x2, y2, w2, h2 = box2

        # Find overlap rectangle
        x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
        y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

        return x_overlap * y_overlap  # Overlapping area

    def total_overlap(self, boxes):
        """Compute total overlapping area between all boxes."""
        overlap_sum = 0
        for box1, box2 in combinations(boxes, 2):
            overlap_sum += self.compute_overlap(box1, box2)
        return overlap_sum

    def optimal_grid_size(self, boxes):
        """
        Determine the best grid size based on box overlaps and sizes.
        """
        num_boxes = len(boxes)

        if num_boxes == 0:
            return 1, 1  # No boxes, default to 1x1 grid

        # Compute average box dimensions
        avg_box_width = np.mean([w for _, _, w, _ in boxes])
        avg_box_height = np.mean([h for _, _, _, h in boxes])

        # Compute total overlap to adjust grid size
        overlap_area = self.total_overlap(boxes)

        # Base grid estimate using average box size
        rows = max(1, int(self.img_height / avg_box_height))
        cols = max(1, int(self.img_width / avg_box_width))

        # If overlap is significant, increase grid density
        overlap_threshold = 0.2 * (
            self.img_width * self.img_height
        )  # 20% of image area
        if overlap_area > overlap_threshold:
            rows = min(rows * 2, num_boxes)  # Increase rows
            cols = min(cols * 2, num_boxes)  # Increase cols

        return rows, cols
