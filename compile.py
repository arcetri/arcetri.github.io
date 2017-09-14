from jinja2 import Environment, BaseLoader, Template, FileSystemLoader

TEMPLATES_DIR = 'templates/'

class Page(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
              setattr(self, key, value)

def compile_html(old_name, new_name, data):
    with open(TEMPLATES_DIR + old_name, 'rb') as f:
        text = f.read()

    output = Environment(loader = FileSystemLoader(TEMPLATES_DIR)).get_template(old_name).render(data)

    with open(new_name, 'wb') as f:
        f.write(output)

env = Environment()
env.loader = FileSystemLoader('.')

pages = [
    Page(old_name='index_template.html', new_name='index.html', data = { 'title': 'Home' }),
    Page(old_name='about_template.html', new_name='about.html', data = { 'title': 'About' }),
    Page(old_name='contacts_template.html', new_name='contacts.html', data = { 'title': 'Contacts' }),
    Page(old_name='faq_template.html', new_name='faq.html', data = { 'title': 'FAQ' }),
    Page(old_name='help_template.html', new_name='help.html', data = { 'title': 'Help' }),
    Page(old_name='index_template.html', new_name='index.html', data = { 'title': 'Index' }),
    Page(old_name='projects_template.html', new_name='projects.html', data = { 'title': 'Projects' })
]

for page in pages:
    compile_html(page.old_name, page.new_name, page.data)
