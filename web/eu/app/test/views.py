
from . import test

@test.route("/")
def index():
	return "test index"

@test.route("/show_id/<id>")
def show_id(id):
	return "test show_id: %s" % id
	
