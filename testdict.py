from db import session, Product


def query():
	
	data = {}
	
	for item  in session.query(Product):
		id = item.id
		data[id] = {
			'id': item.id,
			'name': item.name,
			'price': item.price,
			'desc': item.description,
			'image': item.image
	}
	return print(data)
	
query()
