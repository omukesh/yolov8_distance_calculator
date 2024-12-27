# CCTV Distance Estimation

This project uses a YOLOv8 segmentation model to estimate the distance of objects (persons and monitors) from a CCTV camera in real-time.

## Features

*   **Object detection and segmentation:** Detects and segments persons and monitors in CCTV footage using YOLOv8.
*   **Distance estimation:** Calculates the distance of detected objects from the camera using the perceived width and known width of the objects.
*   **Real-time processing:** Processes the CCTV stream in real-time to provide continuous distance estimations.
*   **Visualization:** Displays the video feed with bounding boxes around detected objects and their estimated distances.

## Requirements

*   Python 3.8 or higher
*   ultralytics
*   opencv-python
*   numpy

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/omukesh/yolov8_distance_calculator
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **CCTV URL:**
    *   Create a file named `config.py` in the project directory.
    *   Add your CCTV URL to `config.py`:
        ```python
        CCTV_URL = "your_cctv_url" 
        ```
2.  **Focal Length Calibration:**
    *   Run the `calculate_focal_length` method in `distance_calculator.py`.
    *   Place a known-sized object at a known distance from the camera.
    *   Measure the pixel width of the object in the captured frame.
    *   Update the `calculate_focal_length` method with the measured pixel width and known values.

## Usage

1.  Run the application:
    ```bash
    python yolo_distance.py
    ```
2.  The application will open a window displaying the CCTV footage with bounding boxes and distance estimations.
3.  Press 'q' to exit the application.

## Notes

*   Ensure the class IDs for "Person" and "Monitor" are correct for your YOLOv8 model.
*   Adjust the `known_width` value in `distance_calculator.py` if necessary.
*   Accurate focal length calibration is crucial for accurate distance estimation.
*   Performance may vary depending on hardware and scene complexity.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is done for educational and research purpose.
