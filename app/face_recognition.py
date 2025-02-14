import cv2
import face_recognition

def capture_and_recognize_face():
    # Capture video from webcam
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it
    known_image = face_recognition.load_image_file("known_face.jpg")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            # Compare the face with the known face
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
            if matches[0]:
                print("Authenticated!")
                return True

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()
    return False
