from ultralytics import YOLO
import cv2

# Load the model
model = YOLO('best.pt')

# Open video file
cap = cv2.VideoCapture('video.mp4')

# Define the codec and create VideoWriter object
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' for .avi files
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break  

    # Perform inference
    results = model(frame)
    result = results[0]

    # Annotate frame
    annotated_frame = result.plot() 

    # Write the annotated frame to the output file
    out.write(annotated_frame)

    # Display the frame (optional)
    cv2.imshow('YOLO Inference', annotated_frame)
    
    # Exit on pressing ESC key
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
