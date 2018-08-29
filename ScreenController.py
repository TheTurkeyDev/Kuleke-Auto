# Code referenced from https://github.com/linusg/rpi-backlight
# Modified to remove gui and cli code that was not needed for this case
import os
import time
import platform

PATH = "/sys/class/backlight/rpi_backlight/"


def _perm_denied():
    print("Permission was denied!")


def _get_value(name):
    if platform.system() == 'Linux':
        try:
            with open(os.path.join(PATH, name), "r") as f:
                return f.read()
        except (OSError, IOError) as err:
            if err.errno == 13:
                _perm_denied()
    return 0


def _set_value(name, value):
    if platform.system() == 'Linux':
        try:
            with open(os.path.join(PATH, name), "w") as f:
                f.write(str(value))
        except (OSError, IOError) as err:
            if err.errno == 13:
                _perm_denied()


def get_actual_brightness():
    """Return the actual display brightness.
    :return: Actual brightness value.
    :rtype: int
    """

    return int(_get_value("actual_brightness"))


def get_max_brightness():
    """Return the maximum display brightness.
    :return: Maximum possible brightness value.
    :rtype: int
    """

    return int(_get_value("max_brightness"))


def set_brightness(value, smooth=False, duration=1):
    """Set the display brightness.
    :param value: Brightness value between 11 and 255
    :param smooth: Boolean if the brightness should be faded or not
    :param duration: Fading duration in seconds
    """

    max_value = get_max_brightness()
    if not isinstance(value, int):
        raise ValueError(
            "integer required, got '{}'".format(type(value)))
    if not 10 < value <= max_value:
        raise ValueError(
            "value must be between 11 and {}, got {}".format(max_value, value))

    if smooth:
        if not isinstance(duration, (int, float)):
            raise ValueError(
                "integer or float required, got '{}'".format(type(duration)))
        actual = get_actual_brightness()
        diff = abs(value - actual)
        while actual != value:
            actual = actual - 1 if actual > value else actual + 1

            _set_value("brightness", actual)
            time.sleep(duration / diff)
    else:
        _set_value("brightness", value)
