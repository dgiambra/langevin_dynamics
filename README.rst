===============================
Langevin Dynamics Simulator
===============================

.. image:: https://img.shields.io/travis/dgiambra/langevin_dynamics.svg
        :target: https://travis-ci.org/dgiambra/langevin_dynamics
.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://pyup.io/repos/github/dgiambra/langevin_dynamics/shield.svg
        :target: https://pyup.io/repos/github/dgiambra/langevin_dynamics/
        :alt: Updates
.. image:: https://coveralls.io/repos/github/dgiambra/langevin_dynamics/badge.svg?branch=master
        :target: https://coveralls.io/github/dgiambra/langevin_dynamics?branch=master
.. image:: https://codecov.io/gh/dgiambra/langevin_dynamics/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/dgiambra/langevin_dynamics

Langevin Dynamics Simulator


* Free software: MIT license
* Created for CHE 477 at University of Rochester


Features
--------

* Contains code for a one dimensional Langevin Dynamics Simulator
* Functions are all documented on necessary inputs
* Potential energy must be input as a text file, with the first column being an index, the second the time, third column if the Potential Energy, and the forth column is the Force, the position must be incrememnted by .01
* Simulation uses SI units
* Results are written to a text file, function also returns three lists of pertinent information
* Tests include setup, teardown, function runs, number of iterations and type of output

Credits
---------
* **Dominic Giambra** - **dgiambra@u.rochester.edu**
* Dr. A White (UR CHE 477)
* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
