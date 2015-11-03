#!/bin/bash

apt-get install -y python-pip libboost-all-dev git cmake
rm -fr yaml-cpp/
git clone https://github.com/jbeder/yaml-cpp.git
cd yaml-cpp/
mkdir build
cd build/
export CXXFLAGS="$CXXFLAGS -fPIC"
cmake ..
make
cp -f libyaml-cpp.a /usr/lib/x86_64-linux-gnu/
cp -fr ../include/yaml-cpp/ /usr/include/
