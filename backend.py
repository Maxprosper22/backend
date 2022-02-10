import cherrypy
import os
from db import Product, session
from pageLoader import home, details

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
	return data


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
	

class Backend:
	@cherrypy.expose
	#@cherrypy.tools.json_out()
	def index(self):
		return "Hello world"
	
	@cherrypy. expose
	@cherrypy.tools.json_out()
	def getId(self, id):
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
cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', '5000')),
})
cherrypy.quickstart(Backend(), '/', conf)