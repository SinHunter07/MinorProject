import cv2   # OpenCV
import os
import time
import uuid

# Set absolute path for image storage
IMAGES_PATH = r'C:\Users\user\OneDrive\Desktop\minorproject\Tensorflow\workspace\images\collectedimages'

labels = ['hello', 'thanks', 'yes', 'no', 'i love you']
number_imgs = 15  # Number of images per label

for label in labels:
    # Create label directory
    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    # Start capturing images
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Error: Failed to capture frame.")
            break

        # Save image
        imagename = os.path.join(label_path, f"{label}_{uuid.uuid1()}.jpg")
        print(f"Saving image to: {imagename}")

        if not cv2.imwrite(imagename, frame):
            print(f"Error: Failed to save image to {imagename}")
        else:
            print(f"Image saved successfully: {imagename}")

        # Display the frame
        cv2.imshow('frame', frame)
        time.sleep(2)

        # Stop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()
