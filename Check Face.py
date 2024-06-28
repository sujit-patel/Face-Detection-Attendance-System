import cv2
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Directory where images are saved
img_dir = "img"

# Load saved face images and their corresponding IDs
saved_faces = {}
for img_name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, img_name)
    if os.path.isfile(img_path):
        img_id, _ = os.path.splitext(img_name)
        img_id = img_id.lower()  # Convert to lowercase to match filename case
        img_id = img_id.replace(" ", "_")  # Replace spaces with underscores
        saved_faces[img_id] = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces and display IDs or messages
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face_detected = False
            for img_id, saved_face in saved_faces.items():
                # Compare detected face with saved faces
                result = cv2.matchTemplate(gray[y:y+h, x:x+w], saved_face, cv2.TM_CCOEFF_NORMED)
                _, confidence, _, _ = cv2.minMaxLoc(result)
                if confidence > 0.7:  # Threshold for confidence
                    cv2.putText(frame, f"ID: {img_id}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    face_detected = True
                    break
            if not face_detected:
                cv2.putText(frame, "Save your face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
