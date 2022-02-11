from jinja2 import FileSystemLoader, Environment

#from backend import query

loader = FileSystemLoader('templates')

env = Environment(loader=loader)

nav = env.get_template('navbar.html')
home = env.get_template('home.html')
details = env.get_template('details.html')
footer = env.get_template('footer.html')