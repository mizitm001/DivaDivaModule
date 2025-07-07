from setuptools import setup, find_packages

setup(
    name="DivaDivaModule",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'divadivamodule = divadivamodule',
        ],
    },
)
