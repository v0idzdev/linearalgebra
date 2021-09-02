from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Linear algebra tools'
LONG_DESCRIPTION = 'Linear algebra tools, including 2D vectors and matrices'


setup(  # Setting up

    # the name must match the
    # folder name 'linalgebra'

    name="linalgebra",
    version=VERSION,
    author="Matthew G. Flegg",
    author_email="<matthewflegg@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    # add any additional packages that need
    # to be installed along with your package

    keywords=['python', 'package'],
    classifiers=[  # Classifiers

        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ]
)
