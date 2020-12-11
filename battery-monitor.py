import time
import os

import board
from adafruit_lc709203f import LC709023F
from prometheus_client import start_http_server, Gauge


sensor = LC709023F(board.I2C())

VOLTAGE = Gauge('voltage','Voltage of the battery (Volts)')
PERCENTAGE = Gauge('percentage','Percentage of the battery remaining (%)')
DEBUG = os.getenv('DEBUG', 'false') == 'true'
SECONDS_BETWEEN_READINGS = int(os.getenv('SECONDS_BETWEEN_READINGS', '5'))

print('## LC709023F battery monitor ##')
print(f'Sensor IC version: {hex(sensor.ic_version)}')

start_http_server(addr='0.0.0.0', port=8001)

while True:
    voltage_reading = sensor.cell_voltage
    percentage_reading = sensor.cell_percent
    if DEBUG:
        print(f'Battery: {voltage_reading} Volts / {percentage_reading}%')
    VOLTAGE.set(voltage_reading)
    PERCENTAGE.set(percentage_reading)
    time.sleep(SECONDS_BETWEEN_READINGS)
