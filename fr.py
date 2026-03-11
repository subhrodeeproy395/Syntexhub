import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)
tip_ids = [4, 8, 12, 16, 20]

while True:

    success, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    gesture = "None"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):

                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)

                lm_list.append((cx, cy))

            fingers = []

            # Thumb
            if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0]-1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for id in range(1,5):

                if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id]-2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Gesture classification
            if fingers == [0,0,0,0,0]:
                gesture = "Fist"
                action = "Pause"

            elif fingers == [1,1,1,1,1]:
                gesture = "Open Palm"
                action = "Play"

            elif fingers == [1,0,0,0,0]:
                gesture = "Thumbs Up"
                action = "Volume Up"

            else:
                action = "None"

            cv2.putText(img, f'Gesture: {gesture}', (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.putText(img, f'Action: {action}', (10,100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Hand Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()