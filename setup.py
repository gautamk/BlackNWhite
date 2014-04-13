from setuptools import setup, find_packages

setup(
    name='blacknwhite',
    version='0.0.2',
    packages=find_packages(),
    license='http://opensource.org/licenses/MIT',
    author='gautam',
    author_email='gautam.nitheesh@gmail.com',
    description='Simple opinionated Static Site generator',
    install_requires=["Markdown==2.4","Jinja2==2.7.2"],
    scripts = ["scripts/blacknwhite"]
)
