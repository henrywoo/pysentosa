#!/bin/bash

apt-get install twine -y

pip uninstall pysentosa --yes

rm -fr build/ dist/ pysentosa.egg-info/

python setup.py bdist_egg

python setup.py sdist build

twine upload --username wufuheng dist/pysentosa*

pip install -U pysentosa
#easy_install dist/pysentosa-0.1.26-py2.7.egg
