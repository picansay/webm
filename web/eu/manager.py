#!/usr/bin/env python

import os,sys
sys.path.append( "%s/scripts"%os.path.abspath('.'))

reload(sys)
sys.setdefaultencoding('utf8') 
from flask import Flask

from app import create_app
from flask.ext.script import Manager

import log

log.set_logger(level = 'DEBUG')

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


if __name__=="__main__":
	manager.run()
