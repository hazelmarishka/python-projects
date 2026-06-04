import cv2

# Load image
image = cv2.imread("hc.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangles
for (x, y, w, h) in faces:

    cv2.rectangle(
        image,
        (x, y),
        (x+w, y+h),
        (255, 0, 0),
        2
    )

# Show image
cv2.imshow("Faces", image)

cv2.waitKey(0)
cv2.destroyAllWindows()