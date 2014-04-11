from setuptools import setup, find_packages

setup(
    name='blacknwhite',
    version='0.0.1',
    packages=find_packages(),
    license='http://opensource.org/licenses/MIT',
    author='gautam',
    author_email='gautam.kumar@orangescape.com',
    description='Simple opinionated Static Site generator',
    install_requires=["Markdown==2.4"],
    scripts = ["scripts/blacknwhite"]
)
