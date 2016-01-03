from setuptools import find_packages
from setuptools import setup

setup(
    name='machination',
    version='0.1',
    description='machination',
    classifiers=[],
    keywords='',
    author='Emerson Matson',
    author_email='emersonn@uw.edu',
    url='',
    packages=['machination'],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    extras_require={
        'test': [
            'mock',
            'nose'
        ]
    }
)
