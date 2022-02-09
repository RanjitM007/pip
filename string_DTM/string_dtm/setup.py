from matplotlib.style import library
from setuptools import setup

setup(name='string_dtm',
        version='0.3.0',
        description='Handeling strings in datetime',
        packages=['string_dtm'],
        author_email='ranjitmaity95@gmail.com',
        zip_safe=False,
        long_description_content_type="text/markdown",
        long_description=open('README.md').read(),
        )