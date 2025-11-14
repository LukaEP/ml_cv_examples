import cv2
import numpy as np
import pyautogui

lower_orange = np.array([0, 200, 110])
upper_orange = np.array([20, 255, 250])

kernel = np.ones((7,7), np.uint8)

cam = cv2.VideoCapture(0)

def get_max_orange_contour(frame):
    orange_mask = get_orange_mask(frame)

    contours, _ = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        return max(contours, key=cv2.contourArea), True
    else:
        return None, False

def get_orange_mask(frame):
    orange_mask = cv2.inRange(frame, lower_orange, upper_orange)

    orange_mask = cv2.erode(orange_mask, kernel, iterations = 1)
    orange_mask = cv2.dilate(orange_mask, kernel, iterations = 2)

    return orange_mask

def mins_and_maxes_x_and_y_in_contour(contornos):
    min_x = max_x = min_y = max_y = None

    for c in contornos:
        if min_x == None or c[0][0] < min_x:
            min_x = c[0][0]
        if max_x == None or c[0][0] > max_x:
            max_x = c[0][0]
        if min_y == None or c[0][1] < min_y:
            min_y = c[0][1]
        if max_y == None or c[0][1] > max_y:
            max_y = c[0][1]

    return min_x, max_x, min_y, max_y

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    max_contorno, found_orange = get_max_orange_contour(hsv_frame)

    frame_height = frame.shape[0]
    move_threshdold = 75
    frame_width = frame.shape[1]
    half_frame_width = frame_width // 2

    cv2.line(frame, (half_frame_width - move_threshdold, 0), (half_frame_width - move_threshdold, frame_height), (255, 0, 255), 2)
    cv2.putText(frame, 'move_left', (40, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, 'stay_still', (half_frame_width - move_threshdold + 5, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.line(frame, (half_frame_width + move_threshdold, 0), (half_frame_width + move_threshdold, frame_height), (255, 0, 255), 2)
    cv2.putText(frame, 'move_right', (half_frame_width + move_threshdold + 40, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if found_orange:
        M = cv2.moments(max_contorno)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 10, (255, 0, 255), -1)


            if cx > (half_frame_width + move_threshdold):
                cv2.putText(frame, 'Moved right', (20, frame_height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                pyautogui.keyDown('right')
            elif cx < (half_frame_width - move_threshdold):
                cv2.putText(frame, 'Moved left', (20, frame_height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                pyautogui.keyDown('left')
            else:
                cv2.putText(frame, 'Stayed still', (20, frame_height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                pyautogui.keyUp('right')
                pyautogui.keyUp('left')

        min_x, max_x, min_y, max_y = mins_and_maxes_x_and_y_in_contour(max_contorno)

        cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (0, 255, 0), 3)

    cv2.imshow("Webcam original", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()