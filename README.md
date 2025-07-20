# YOLOv8 Object Detection for AMA Computer College Students

This project provides a hands-on introduction to real-time object detection using the YOLOv8 model. This guide will walk you through setting up your development environment and running the project.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, you need to have Python and Visual Studio Code installed on your computer.

### 1. Installing Visual Studio Code

Visual Studio Code (VS Code) is a free and powerful code editor that we will use for this project.

1.  **Download VS Code:**
    -   Go to the official VS Code website: [https://code.visualstudio.com/](https://code.visualstudio.com/)
    -   Download the installer for your operating system (Windows, macOS, or Linux).

2.  **Install VS Code:**
    -   Run the installer you downloaded.
    -   Follow the on-screen instructions. It is recommended to keep the default settings, especially the option to "Add to PATH" (on Windows).

3.  **Install Python Extension for VS Code:**
    -   Open VS Code.
    -   Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
    -   Search for "Python" and install the extension provided by Microsoft.

### 2. Installing Python

Python is the programming language we will use.

1.  **Download Python:**
    -   Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    -   Download the latest stable version of Python (e.g., Python 3.9 or higher).

2.  **Install Python:**
    -   Run the Python installer.
    -   **Important:** On the first screen of the installer, make sure to check the box that says **"Add Python to PATH"**. This will make it easier to run Python from the command line.
    -   Click "Install Now" and follow the on-screen instructions.

3.  **Verify the Installation:**
    -   Open a new terminal or command prompt.
    -   Type `python --version` and press Enter. You should see the Python version you installed.

## Project Setup

Now that you have the prerequisites, let's set up the project.

1.  **Download the Project:**
    -   Download the project files as a ZIP folder and extract them to a location of your choice (e.g., your Desktop).

2.  **Open the Project in VS Code:**
    -   Open VS Code.
    -   Go to `File > Open Folder` and select the folder where you extracted the project files.

3.  **Install Required Libraries:**
    -   Open the terminal in VS Code by going to `Terminal > New Terminal`.
    -   In the terminal, run the following command to install the necessary Python libraries from the `requirements.txt` file:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Download YOLOv8 Model Weights:**
    -   The project is configured to use `yolov8n.pt` by default. This file is included in the project.
    -   If you want to use a different model, you can download it from the [Ultralytics YOLOv8 repository](https://github.com/ultralytics/ultralytics) and place it in the project's root directory.

## How to Run

1.  **Add a Video:**
    -   Create a folder named `videos` in the project directory.
    -   Place any video file you want to analyze inside this `videos` folder.

2.  **Run the Script:**
    -   Make sure you are in the VS Code terminal.
    -   Run the main script with the following command:
        ```bash
        python main.py
        ```

3.  **Follow On-Screen Prompts:**
    -   The script will ask you to choose a video source:
        -   Enter `1` to select a video from the `videos` folder.
        -   Enter `2` to provide a full file path to a video on your computer.

4.  **View the Output:**
    -   A new window will open, showing the video with objects being detected and labeled in real-time.

5.  **Quit the Program:**
    -   To stop the video and close the application, press the **'q'** key on your keyboard.

## Project Structure

```
.
├── main.py             # The main Python script for object detection
├── requirements.txt    # A list of project dependencies (Python libraries)
├── yolov8n.pt          # The pre-trained YOLOv8 model weights
└── videos/             # A directory to store your video files
    └── your_video.mp4
```