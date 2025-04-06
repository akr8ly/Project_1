import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
  print("brr brr")
while True:
  ret, frame = cap.read()
  if not ret:
    print ("brr brr")
    break

  cv2.imshow("frame", frame)
  if cv2.waitKey(1) & 0xFF == 32:
    print("press space bar to quit")
    break
cap.release()
cv2.destroyAllWindows()

    