import cv2
import numpy as np
import config

cctv_url = config.CCTV_URL

class DistanceCalculator:
    def __init__(self, known_width_person, known_width_monitor, focal_length=None):
        self.known_width_person = known_width_person
        self.known_width_monitor = known_width_monitor
        self.focal_length = focal_length or self.calculate_focal_length()

    def calculate_focal_length(self, img_width=868, known_distance=1, known_width=0.2):
        cap = cv2.VideoCapture(cctv_url)  # Replace with your CCTV URL
        ret, frame = cap.read()
        cap.release()

        # and measure its pixel width in the frame
        pixel_width = 200  # Measure this from the frame
        self.focal_length = (pixel_width * known_distance) / known_width
        return self.focal_length

    def calculate_distance(self, perceived_width, known_width):
        if self.focal_length is None:
            raise ValueError("Focal length needs to be calculated")
        return (known_width * self.focal_length) / perceived_width

    def calculate_distance_person(self, box):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        perceived_width = x2 - x1
        return self.calculate_distance(perceived_width, self.known_width_person)

    def calculate_distance_monitor(self, box):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        perceived_width = x2 - x1
        return self.calculate_distance(perceived_width, self.known_width_monitor)
