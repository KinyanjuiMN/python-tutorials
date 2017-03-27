try:
   from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'Bank Application handles members accounts',
    'author': '@KinyanjuiMN',
    'url': 'URL to get it at.', 'download_url': 'Where to download it.', 'author_email': 'knjonjo@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'], 'packages': ['Bank'],
    'scripts': [],
   'name': 'Bank Application'
}

setup(**config)
