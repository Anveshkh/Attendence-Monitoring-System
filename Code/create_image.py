
import cv2

name = input("Enter the name of person you are recording :- ")
count = 0

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    # frame = cv2.resize(frame, (450, 450))

    cv2.imshow('frame', frame)
    if count == 0:
        cv2.imwrite(f"../ImagesAttendance/{name}.jpg", frame)

    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

