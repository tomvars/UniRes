from setuptools import setup, find_packages


setup(
    name='unires',
    version='0.1a',
    packages=find_packages(),
    url='https://github.com/brudfors/UniRes',
    author='Mikael Brudfors',
    author_email='brudfors@gmail.com',
    entry_points={'console_scripts': ['unires=unires._cli:run']},
    description='UniRes: Unified Super-Resolution of Neuroimaging Data',
    python_requires='>=3.6'

)
