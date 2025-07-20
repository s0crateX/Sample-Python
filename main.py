import cv2  # OpenCV library for computer vision tasks like video capture and image processing
from ultralytics import YOLO  # YOLO (You Only Look Once) object detection model
import os  # OS library to work with files and directories

# Function to ask the user where to get the video (from folder or local path)
def get_video_source():
    print("1) Select a video from the 'videos' folder")
    print("2) Paste a local file path")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        video_folder = "videos"  # folder where video files should be placed

        # Check if the folder exists
        if not os.path.exists(video_folder) or not os.path.isdir(video_folder):
            print(f"Error: The '{video_folder}' directory does not exist.")
            return None

        # Get list of video files in the folder
        videos = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]

        if not videos:
            print(f"No videos found in the '{video_folder}' directory.")
            return None

        # Show all available videos in the folder
        print("\nAvailable videos:")
        for i, video_name in enumerate(videos):
            print(f"{i + 1}) {video_name}")

        # Ask user to choose one of the listed videos
        video_choice = input(f"Choose a video (1-{len(videos)}): ").strip()
        try:
            video_index = int(video_choice) - 1
            if 0 <= video_index < len(videos):
                return os.path.join(video_folder, videos[video_index])  # Return full path of chosen video
            else:
                print("Invalid selection.")
                return None
        except ValueError:
            print("Invalid input.")
            return None

    elif choice == "2":  # User chooses to input a full path manually
        path = input("Enter local video path: ").strip()
        return path  # Return path entered by user
    else:
        print("Invalid choice, defaulting to webcam (0)")
        return 0  # If input is invalid, fallback to webcam as the video source

# Main function where everything happens
def main():
    source = get_video_source()  # Ask user for video source
    cap = cv2.VideoCapture(source)  # Open video capture (file or webcam)

    if not cap.isOpened():  # Check if the video source is working
        print(f"Error: cannot open video source '{source}'")
        return

    model = YOLO('yolov8n.pt')  # Load the YOLOv8 model (n = nano, smallest version)

    # target_classes = ['car']  # Define target classes for detection

    # # Get the integer indices for the target classes from the model's names
    # class_indices = [i for i, name in model.names.items() if name in target_classes]

    while True:
        ret, frame = cap.read()  # Read one frame from the video
        if not ret:  # If there's no frame (end of video or error), exit loop
            print("End of stream or unable to get frame.")
            break

        # Run YOLO object detection, filtering for the target classes
        results = model(frame)[0] #, classes=class_indices
        annotated = results.plot()  # Draw boxes and labels on detected objects

        # Resize the frame so it fits better on screen
        display_width = 960  
        h, w, _ = annotated.shape 
        display_height = int(h * (display_width / w)) 
        display_frame = cv2.resize(annotated, (display_width, display_height))

        # Show the video with detection in a window
        cv2.imshow("YOLOv8 Detection", display_frame)

        # Wait for 1 millisecond, break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the video source
    cv2.destroyAllWindows()  # Close the video window

# Run the main function if the script is being run directly
if __name__ == "__main__":
    main()
