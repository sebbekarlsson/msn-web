from distutils.core import setup
import setuptools


setup(
    name='msnweb',
    version='1.0',
    install_requires=[
        'flask',
        'flask_wtf',
        'wtforms',
        'pymongo'
    ],
    packages=[
        'msnweb'
    ],
    entry_points={
    },
   )
