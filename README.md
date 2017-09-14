# Arcetri cluster official site

Presentation site for the CISCO Arcetri cluster
Avaliable at [arcetri.github.io](http://arcetri.github.io)

### Prerequisites

Things you need to install: [Jinja2](http://jinja.pocoo.org)

```
pip install jinja2
```

### Cloning and modifying code

Run this in your terminal

```
git clone https://github.com/arcetri/arcetri.github.io.git
```

Notice: .html files in a root directory are generated automatically - do not change them!

Instead, modify files in templates/ directory. Do not forget to make changes in compile.py file to compile new files.

## Deployment

Run this command in terminal in a root project directory

```
python compile.py
```

## Built With

* [Bootstrap](http://getbootstrap.com) - The web framework used
* [Jinja2](http://jinja.pocoo.org) - Templating language for Python

## Authors

* **Bogdan Salyp** - *Initial work* - [PurpleBooth](https://github.com/trntga)

## Acknowledgments

* Hat tip to anyone who's code was used
