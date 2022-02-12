from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('templates')
env = Environment(loader=loader)

home = env.get_template('home.html').render(name ="Max P")
nav = env.get_template('navbar.html').render()

with open('index.html', 'w') as f:
    f.write(home)
    