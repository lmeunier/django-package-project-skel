from setuptools import setup, find_packages

version='0.1.0'

setup(
    name='myproject',
    version=version,
    description='Django skeleton project',
    long_description=__doc__,
    author='Laurent Meunier',
    author_email='laurent@deltalima.net',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django==1.5'],
)

