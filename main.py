import cv2

# Read the orthomosaic image
image = cv2.imread('images/orthomosaic.jpg')

# Minimum area threshold for filtering contours
min_area = 100

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area or other criteria
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Draw contours on the original image
cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Border Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
