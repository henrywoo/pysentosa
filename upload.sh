#!/bin/bash

apt-get install twine -y

pip uninstall pysentosa --yes

rm -fr build/ dist/ pysentosa.egg-info/

python setup.py bdist_egg

python setup.py sdist build

twine upload --username wufuheng dist/pysentosa*

pip install -U pysentosa
