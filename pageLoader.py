from jinja2 import FileSystemLoader, Environment

from db import Product, session

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

loader = FileSystemLoader('templates')

env = Environment(loader=loader)

nav = env.get_template('navbar.html').render()
home = env.get_template('home.html').render(data=query())
details = env.get_template('details.html').render()
footer = env.get_template('footer.html').render()