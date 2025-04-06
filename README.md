# Control-LED-with-Fingger-Recognition
# ✋ Finger Detection & LED Control via ESP8266 (HTTP)

Control 5 LEDs using just your fingers!  
This project combines real-time hand tracking with MediaPipe and sends HTTP requests to an ESP8266 to turn on LEDs based on the number of fingers detected.

---

## 🎯 Features
- Real-time hand & finger detection using webcam
- Control up to 5 LEDs based on finger count
- Wireless communication over local WiFi via HTTP
- Lightweight web server hosted on ESP8266 (Wemos D1 Mini)

---

## 🛠️ Hardware Required
- Laptop/PC with webcam
- ESP8266 (Wemos D1 Mini)
- 5x LEDs with 1k resistors
- Breadboard & jumper wires
- WiFi connection (local)

---

## 🧰 Software Requirements
- [MediaPipe](https://chuoling.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [Requests](https://docs.python-requests.org/en/latest/)

Install them via pip:
```bash
pip install mediapipe opencv-python requests
