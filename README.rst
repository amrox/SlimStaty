=========
SlimStaty
=========


.. .. image:: https://img.shields.io/pypi/v/slimstaty.svg
        :target: https://pypi.python.org/pypi/slimstaty

.. .. image:: https://img.shields.io/travis/amrox/slimstaty.svg
        :target: https://travis-ci.org/amrox/slimstaty

.. .. image:: https://readthedocs.org/projects/slimstaty/badge/?version=latest
        :target: https://slimstaty.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


SlimStaty is a toy project to generate state machine implementations from a YAML representation::

 statemachine:
  name: "turnstile"
  events:
    - { name: coin, from: locked, to: unlocked }
    - { name: push, from: unlocked, to: locked }


Into Java and Objective-C, currently.  Very much a work in progress.

* Free software: MIT license
* Documentation: https://slimstaty.readthedocs.io.



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
