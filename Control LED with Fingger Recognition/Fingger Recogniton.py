import cv2
import mediapipe as mp
import requests

# IP Wemos (ubah sesuai IP kamu)
IP_WEMOS = "http://192.168.100.154"
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def hitung_jari(hand_landmarks, handedness):
    tips = [4, 8, 12, 16, 20]
    pips = [3, 6, 10, 14, 18]
    jari = 0
    if handedness.classification[0].label == 'Right':
        if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[pips[0]].x:
            jari += 1
    else:
        if hand_landmarks.landmark[tips[0]].x > hand_landmarks.landmark[pips[0]].x:
            jari += 1
    for tip, pip in zip(tips[1:], pips[1:]):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            jari += 1
    return jari

def kirim_ke_wemos(jumlah):
    try:
        url = f"{IP_WEMOS}/led?jari={jumlah}"
        r = requests.get(url, timeout=1)
        print("Kirim ke Wemos:", r.status_code)
    except Exception as e:
        print("Gagal kirim:", e)

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        total_jari = 0
        if result.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(result.multi_hand_landmarks):
                handedness = result.multi_handedness[i]
                total_jari += hitung_jari(hand_landmarks, handedness)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                      mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=3, circle_radius=6),
                      mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=3))             
        cv2.putText(frame, f'Jari: {total_jari}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.imshow('Deteksi Jari', frame)
        kirim_ke_wemos(total_jari)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
