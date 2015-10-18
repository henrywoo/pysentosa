#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Fuheng(henry.woo@outlook.com)'
__version__= '0.1.24'

from datetime import datetime
import os
import urllib
import yaml
import netifaces as ni

def __get_ip():
  try:
    return ni.ifaddresses('eth0')[2][0]['addr']
  except ValueError, e:
    return ni.ifaddresses('em0')[2][0]['addr']

def __load_yml(conf_dir):
  if not os.path.exists(conf_dir):
      os.mkdir(conf_dir)
  if not os.path.exists(conf_dir+'sentosa.yml'):
      urllib.urlretrieve(
          "https://raw.githubusercontent.com/henrywoo/qblog/master/sentosa.yml",
          conf_dir + "sentosa.yml")
  if not os.path.exists(conf_dir+'holiday.yml'):
      urllib.urlretrieve(
          "https://raw.githubusercontent.com/henrywoo/qblog/master/holiday.yml",
          conf_dir + "holiday.yml")
  yml_sentosa=yaml.load(open(conf_dir+'sentosa.yml'))
  yml_holiday=yaml.load(open(conf_dir+'holiday.yml'))
  return yml_sentosa, yml_holiday


def __get_symbol():
  _node = yml_sentosa['strategies']
  if _node.has_key("singleta"):
      syms=_node['singleta']
  if _node.has_key("pairs"):
      [syms.extend(s.split('|')[1:3]) for s in _node['pairs']]
  syms=list(set(syms))
  return syms

YMD=datetime.now().strftime("%Y-%m-%d")
CONFDIR = os.path.expanduser("~/.sentosa/")
LOCALIP = __get_ip()
yml_sentosa, yml_holiday = __load_yml(CONFDIR)
SYMBOLS = __get_symbol()
ACCOUNT = yml_sentosa['global']['account']
TRADEINFODIR = yml_sentosa['linux']['TRADEINFODIR'] + os.sep + ACCOUNT
