# Balena battery monitor LC709203F

A BalenaOS LiPo/Lion battery monitor using the LC709203F board from Adafruit.

Based on the [Adafruit example](https://github.com/adafruit/Adafruit_CircuitPython_LC709203F/blob/master/examples/lc709203f_simpletest.py)

## Read errors

If you come across the error: `RuntimeError: CRC failure on reading word`, you might need to [set the I2C clock to 10,000Hz](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/i2c-clock-stretching).

To do this in Balena, add `i2c_arm_baudrate=10000` to the `Device Configuration` tab, `Define DT parameters`, so the full entry is: `"i2c_arm=on","spi=on","audio=on","i2c_arm_baudrate=10000"`
