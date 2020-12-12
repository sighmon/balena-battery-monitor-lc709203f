FROM balenalib/raspberry-pi-alpine-python:latest-build

WORKDIR /usr/src

RUN pip3 install --upgrade setuptools && pip3 install \
  adafruit-circuitpython-lc709203f \
  prometheus_client

CMD modprobe i2c-dev && python3 battery-monitor.py
