# Sensor Data Logger and Broadcaster

## Overview
This Python script (`main.py`) and Arduino firmware (`firmware.ino`) work together to log sensor data from an MPU6050 sensor and broadcast it over UDP. The Python script receives the broadcasted data and logs it into CSV files.

## Prerequisites
- Python 3.x
- Arduino IDE
- MPU6050 sensor
- Arduino board with WiFi capabilities (e.g., ESP8266)

## Installation and Setup

### Python Script (`main.py`)
1. Ensure that Python is installed on your system.
2. Run the script using the command: `python main.py`

### Arduino Firmware (`firmware.ino`)
1. Open `firmware.ino` in the Arduino IDE.
2. Upload the firmware to your Arduino board.

## Usage

### Python Script (`main.py`)
1. Run the Python script to start listening for UDP broadcasts.
2. When prompted, press "Enter" to begin logging sensor data.
3. The script will create CSV files (`logX.csv`) containing the sensor data every 4 seconds.

### Arduino Firmware (`firmware.ino`)
1. Connect the MPU6050 sensor to your Arduino board.
2. Adjust the WiFi credentials in the firmware (`ssid` and `pass`).
3. Upload the firmware to your Arduino board.

## Additional Notes
- The Arduino firmware reads sensor data from the MPU6050 sensor and broadcasts it over UDP to IP `255.255.255.255` and port `2255`.
- The Python script listens for UDP broadcasts on port `2255` and logs the received sensor data into CSV files.

## Dependencies
- Python: `numpy`, `pandas`, `matplotlib`
- Arduino Libraries: `WiFi`, `AsyncUDP`, `Adafruit_MPU6050`, `Wire`

Feel free to contribute or report issues!
