
from setuptools import setup

import emailgen

setup(
    name='emailgen',
    packages=['emailgen'],
    version=emailgen.__version__,
    license="Apache",
    description='Email Generation for Humans',
    author='Finnesota LLC',
    author_email='info@finnesota.com',
    url='https://github.com/finnesota/emailgen',
    keywords=["email", "generation", "html", "SaaS", "transactional"],
    install_requires=[
        "jinja2",
        "markdown2"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
)
