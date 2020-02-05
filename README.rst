======
wangls
======


.. image:: https://img.shields.io/pypi/v/wangls.svg
        :target: https://pypi.python.org/pypi/wangls

.. image:: https://img.shields.io/travis/ally-ahmed/wangls.svg
        :target: https://travis-ci.org/ally-ahmed/wangls

.. image:: https://readthedocs.org/projects/wangls/badge/?version=latest
        :target: https://wangls.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A command line tool that gives you the IPs of the devices connected to the same network segment.


* Free software: MIT license
* Documentation: https://wangls.readthedocs.io.


Usage
--------

* Simple scan that returns only IPs.

.. code-block:: console

    $ wangls

.. image:: https://i.imgur.com/SIkQfju.gif

* Scanning your whole network with OS detection might take some time especially if there are many devices connected.

.. code-block:: console

    $ wangls -o

.. image:: https://i.imgur.com/HUNFvrD.png
