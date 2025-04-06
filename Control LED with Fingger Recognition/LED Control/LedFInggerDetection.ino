#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "ssid_wifi/hotspot_kalian";
const char* password = "password_wifi/hotspot_kalian";

ESP8266WebServer server(80);

const int leds[] = {D1, D2, D4, D5, D6};

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  WiFi.begin(ssid, password);
  Serial.print("Menghubungkan ke WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Terhubung. IP:");
  Serial.println(WiFi.localIP());

  server.on("/led", handleLed);
  server.begin();
}

void loop() {
  server.handleClient();
}

void handleLed() {
  if (server.hasArg("jari")) {
    int jumlah = server.arg("jari").toInt();
    jumlah = constrain(jumlah, 0, 5); // maksimal 5 LED

    // Nyalakan LED sesuai jumlah jari
    for (int i = 0; i < 5; i++) {
      digitalWrite(leds[i], i < jumlah ? HIGH : LOW);
    }

    server.send(200, "text/plain", "LED Updated: " + String(jumlah));
    Serial.println("Jumlah jari: " + String(jumlah));
  } else {
    server.send(400, "text/plain", "Argumen jari tidak ditemukan");
  }
}
