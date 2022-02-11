from jinja2 import Environment, FileSystemLoader

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
	return data

loader = FileSystemLoader('templates')

env = Environment(loader=loader)

home = env.get_template('home.html').render(data=query())

fileName = 'index.html'

with open(f"/site/{fileName}", 'w') as f:
	f.write(home)