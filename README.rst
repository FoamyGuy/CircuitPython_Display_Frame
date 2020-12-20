Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-circuitpython-display_frame/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/display_frame/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/foamyguy/Circuitpython_CircuitPython_Display_Frame/workflows/Build%20CI/badge.svg
    :target: https://github.com/foamyguy/Circuitpython_CircuitPython_Display_Frame/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython displayio widget to create a rounded rectangle frame with text label at the top center.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-display_frame/>`_. To install for current user:

.. code-block:: shell

    pip3 install circuitpython-display-frame

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-display-frame

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-display-frame

Usage Example
=============

.. code-block:: python

    import board
    import displayio
    from circuitpython_display_frame import Frame

    display = board.DISPLAY
    main_group = displayio.Group()

    example_frame = Frame(10, 10, display.width // 3, display.height - 16)
    main_group.append(example_frame)

    display.show(main_group)
    while True:
        pass

.. image:: https://github.com/FoamyGuy/CircuitPython_Display_Frame/blob/main/example_image.png?raw=true
    :alt: Example photo

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/foamyguy/Circuitpython_CircuitPython_Display_Frame/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
