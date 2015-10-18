#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from config import yml_sentosa
from pandas.io.sql import read_sql

#https://razvantudorica.com/08/example-for-singleton-decorator-pattern-in-python/
class Singleton:
  def __init__(self, klass):
    self.klass = klass
    self.instance = None
  def __call__(self, *args, **kwds):
    if self.instance == None:
      self.instance = self.klass(*args, **kwds)
    return self.instance

@Singleton
class DBConn:
  connection = None
  def get_connection(self):
    if self.connection is None:
      self.connection = pymysql.connect(host=yml_sentosa['DB']['DBHOST'],
                              port=3306,
                              user=yml_sentosa['DB']['DBUSER'],
                              passwd=yml_sentosa['DB']['DBPASS'],
                              db=yml_sentosa['DB']['DBNAME'])
    return self.connection

class CQuery(object):
    sqlcache = {}

    def __init__(self):
        self.dbconn = DBConn().get_connection()
        self.cur=self.dbconn.cursor()

    def cachedQuery(self, sql):
        if CQuery.sqlcache.has_key(sql):
            return CQuery.sqlcache[sql]
        tmp = read_sql(sql, self.dbconn, index_col='dt')
        CQuery.sqlcache[sql] = tmp
        return tmp

    def Query(self, sql):
        return read_sql(sql, self.dbconn, index_col='dt')

    def execute(self,sql):
        self.cur.execute(sql)


if __name__ == "__main__":
    print DBConn().get_connection()
    result=CQuery().Query("select * from transaction")
    print result
