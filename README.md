# pythonwhat-ext

[![Build Status](https://travis-ci.org/datacamp/pythonwhat-ext.svg?branch=master)](https://travis-ci.org/datacamp/pythonwhat-ext)
[![PyPI version](https://badge.fury.io/py/pythonwhat-ext.svg)](https://badge.fury.io/py/pythonwhat-ext)


Extensions (high-level SCTs) for pythonwhat

[Documentation here](http://pythonwhat-ext.readthedocs.io/).

Including in a DataCamp course
------------------------------

In the course's `requirements.sh`, add

```
# replace 0.0.1 with the appropriate release version
# be sure to use --no-deps flag, so it ONLY installs extension
pip3 install --no-deps pythonwhat-ext==0.0.1
```

To use the extensions in an exercise's SCT, import the function you want into the SCT block of the exercise:

```
from pythonwhat_ext import check_numpy_array

Ex() >> check_numpy_array('x')
```

Deploying to PyPI
----------------------------

Follow these steps

1. Open a PR, merge into master when appropriate.
2. Once merged, increment `__version__ = 0.0.1` to reflect changes ([see semver for guidance](http://semver.org/)).
3. Create a github release labeled `vVERSION`. E.g. `v0.0.1`. (see [here](https://help.github.com/articles/creating-releases/)).


Running tests
-------------

```
pip install -r requirements.txt
# may need to uncomment line below
#pip install -e .
py.test tests
```
