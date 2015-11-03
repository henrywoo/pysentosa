#!/bin/bash

pushd /singapore/research/pysentosa

#rm -fr /usr/local/lib/python2.7/dist-packages/pysentosa
#cp pysentosa /usr/local/lib/python2.7/dist-packages/pysentosa -Rf


#rm -f /usr/lib/python2.7/lib-dynload/pysentosa.so
#cp /singapore/bin/pysentosa.so /usr/lib/python2.7/lib-dynload/
pip uninstall pysentosa --yes
rm -fr build/ dist/ pysentosa.egg-info/
python setup.py bdist_egg
easy_install dist/pysentosa-0.1.27-py2.7.egg
popd
