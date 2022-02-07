import cherrypy
import os
from db import Product, session
#from loopdir import stuff

#print(stuff)

def query():
	data = []
	for item in session.query(Product):
		data.append({
			'id': item.id,
			'name': item.name,
			'price': item.price,
			'desc': item.description,
			'image': item.image
		})
		#print(data)
	return data

info = []
def getproductid():
	for item in session.query(Product):
		info .append({
			'id': item.id,
			'name': item.name,
			'price': item.price,
			'desc': item.description,
			'image': item.image
		})
	return info
#value = query()

#def newUser(value):
#	new = Product(name=value.name, price=value.price)
#	session.add(new)
#	session.commit()

class Backend:
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self):
		return query()
		
	@cherrypy. expose
	@cherrypy.tools.json_out()
	def getId(self, id):
		#stuff=[]
		getproductid()
		
		stuff = session.query(Product).filter(Product.id==id).first()
		print(stuff.id, stuff.name)
		
		datalist = {}
		datalist.update({
			'id': stuff.id,
			'name': stuff.name,
			'price': stuff.price,
			'desc': stuff.description,
			'image': stuff.image
		})
		return datalist
		
#	@cherrypy.expose
#	@cherrypy.tools.json_in()
#	def addUser(self, result):
		#newUser()
#		r = result
#		print(r)
#		return 'Ok'
		
	
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [ ('Access-Control-Allow-Origin', 'http://localhost:3000'),
            ('Content-Type', 'application/json')],
            
            'tools.staticdir.root': os.path.abspath(os.getcwd())
		},

	'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './assets'
	}
}
cherrypy.quickstart(Backend(), '/', conf)