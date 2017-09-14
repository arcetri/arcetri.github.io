from jinja2 import Environment, BaseLoader, Template, FileSystemLoader

TEMPLATES_DIR = 'templates/'

def compile_html(old_name, new_name, data):
    with open(TEMPLATES_DIR + old_name, 'rb') as f:
        text = f.read()

    output = Environment(loader = FileSystemLoader(TEMPLATES_DIR)).get_template(old_name).render(data)

    with open(new_name, 'wb') as f:
        f.write(output)

env = Environment()
env.loader = FileSystemLoader('.')

data = {'title': 'Home'}
compile_html('index_template.html', 'index.html', data)

data = {'title': 'About'}
compile_html('about_template.html', 'about.html', data)

data = {'title': 'Contacts'}
compile_html('contacts_template.html', 'contacts.html', data)

data = {'title': 'FAQ'}
compile_html('faq_template.html', 'faq.html', data)

data = {'title': 'Help'}
compile_html('help_template.html', 'help.html', data)

data = {'title': 'Projects'}
compile_html('projects_template.html', 'projects.html', data)