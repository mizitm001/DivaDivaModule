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
            'divadivamodule = run_divadivamodule:main',  
        ],
    },
)
