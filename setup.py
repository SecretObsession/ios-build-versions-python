#!/usr/bin/env python

from setuptools import setup

setup(
    name="ios-build-versions",
    version="0.2.1",
    description="iOS Version lookup based on build number",
    author="Mike Herold",
    author_email="archangel.herold@gmail.com",
    url="https://github.com/SecretObsession/ios-build-versions-python",
    packages=["iosbuildversions"],
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
