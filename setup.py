from setuptools import setup, find_packages

setup(
    name="DivaDivaModule",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'divadivamodule = divadivamodule:__file__', #i swear to god if this does not work i will kill everyone on this planet
        ],
    },
)
