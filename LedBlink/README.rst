Introduction
============

Grove series driver for control led.

Usage Example
=============

.. code-block:: python

    from grove import grove_led
    import board
    import time

    led = grove_led(board.SCL)
    led.value = 0

    while True:
        led.value = not led.value
        time.sleep(1)

Contributing
============

If you have any good suggestions or comments, you can send issues or PR us.
