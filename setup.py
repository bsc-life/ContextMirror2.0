from setuptools import setup, find_packages
import configparser
import subprocess
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'ContextMirror'


# Setting up
setup(
    name="ContextMirror",
    version=VERSION,
    author="BSC (Miguel Fernández)",
    author_email="<miguel.fernandez@bsc.es>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'pandas','configparser', 'dendropy'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'MirrorTree=ContextMirror.modules.modulo1:mirror_tree',
            'PPCorrelation=ContextMirror.modules.modulo2:modulo2',
            'PartialCorrelation=ContextMirror.modules.modulo3:modulo3',
            'ContextMirror=ContextMirror.modules.modulo4:context_mirror',

        ],
    })
    

#can you add an option to do entry points conditional of the first argument?
