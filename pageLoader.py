from jinja2 import Environment, FileSystemLoader


loader = FileSystemLoader('templates')

env = Environment(loader=loader)

home = env.get_template('home.html').render(data=query(), title="My App", name="Max Prosper")

fileName = 'index.html'

with open(f"site/{fileName}", 'w') as f:
	f.write(home)