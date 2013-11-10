from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='{{ project_name }}',
    version=version,
    description='Django skeleton project',
    long_description=__doc__,
    author='Foo Bar',
    author_email='foobar@example.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django>=1.5'],
    entry_points={
        'console_scripts': [
            '{{ project_name}}_manage = {{ project_name }}.manage:main',
        ],
    }
)
