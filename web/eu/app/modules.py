
from . import db
from flask import url_for


class kfw_device(db.Document):
	name = db.StringField(max_length=255, required=True)
	ip = db.StringField(max_length=255, required=True)
	port = db.IntField(required=True)
	c_date = db.StringField(required=True)

	def __str__(self):
		return "%s" % self.__dict__
		#return "name: %s, ip: %s, port: %s" % (self.name ,self.ip,self.port)


