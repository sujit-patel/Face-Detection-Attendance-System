import cv2
import os

# Function to create folder if it doesn't exist
def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to validate student ID
def validate_student_id(student_id):
    if len(student_id) == 4 and student_id.isdigit():
        return True
    else:
        return False

# Function to capture photo with face detection
def capture_photo_with_face_detection(student_id):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    # Create the "img" folder if it doesn't exist
    create_folder_if_not_exists("img")

    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw green rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Capture Photo with Face Detection", frame)
        
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        
        # Check if the 'q' key is pressed to quit the loop
        if key == ord('q'):
            break
        # Check if the 's' key is pressed to save the image
        elif key == ord('s'):
            # Check if any faces are detected
            if len(faces) > 0:
                # Save the captured image with the provided student ID as part of the filename in the "img" folder
                filename = os.path.join("img", f"{student_id}.jpg")
                cv2.imwrite(filename, frame)
                print("Image saved successfully as", filename)
            else:
                print("No face detected. Image not saved.")
            break

    # Release the camera
    cap.release()

    # Close OpenCV windows
    cv2.destroyAllWindows()

# Ask the user for their 4-digit student ID
while True:
    student_id = input("Enter your 4-digit student ID: ")
    if validate_student_id(student_id):
        break
    else:
        print("Invalid student ID. Please enter a 4-digit number.")

# Call the function to capture photo with face detection
capture_photo_with_face_detection(student_id)
