try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Play and analyze the game blackjack',
    'author': 'Curt Fulwider, Patrick Tomei, KJ Welch',
    'url': 'https://github.com/kj01a/blackjack',
    'dl_url': 'tbd',
    'email': 'ftw-engineering@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['blackjack'],
    'scripts': [],
    'name': 'blackjack'
}

setup(**config)
