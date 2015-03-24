from flask.ext.restplus import Api, Resource, fields
import sys,os
print sys.path
print os.path.abspath('.')
sys.path.append( "%s/scripts"%os.path.abspath('.'))
print sys.path
