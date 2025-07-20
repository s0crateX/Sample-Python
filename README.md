# YOLOv8 Object Detection

This project uses the YOLOv8 model to perform real-time object detection on a video file. The script can process videos from a local folder or a specified file path.

## Requirements

The following libraries are required to run this project:

- `opencv-python`
- `ultralytics`

## Installation

1.  **Clone the repository or download the files.**

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the YOLOv8 model weights:**

    The script uses the `yolov8n.pt` model by default. You can download other models from the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) repository. Make sure the model file (e.g., `yolov8n.pt`) is in the same directory as `main.py`.

## How to Run

1.  **Place your video files** in the `videos` directory. If the directory does not exist, create it.

2.  **Run the script from your terminal:**

    ```bash
    python main.py
    ```

3.  **Follow the on-screen prompts:**
    -   Choose `1` to select a video from the `videos` folder.
    -   Choose `2` to provide a local file path to a video.

4.  A window will open displaying the video with object detection overlays.

5.  Press the **'q'** key to quit the video playback and close the window.

## Project Structure

```
.
├── main.py             # The main script for object detection
├── requirements.txt    # Project dependencies
├── yolov8n.pt          # YOLOv8 model weights (or other versions)
└── videos/             # Directory for video files
    └── example.mp4