Introduction
============

The Led will light when keep the key pressed and will go out when the key is released.

Usage Example
=============

.. code-block:: python

    from grove import grove_led
    from grove import grove_button
    import board
    import time

    btn = grove_button(board.SCL)
    led = grove_led(board.D2)

    while True:
        if btn.value:
            led.value = 1
        else:
            led.value = 0

Contributing
============

If you have any good suggestions or comments, you can send issues or PR us.
