#!/bin/bash

apt-get install -y automake

rm -fr nanomsg_tmp
git clone https://github.com/nanomsg/nanomsg.git nanomsg_tmp
cd nanomsg_tmp
sh autogen.sh
./configure
make
make install

