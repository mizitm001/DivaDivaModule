from setuptools import setup, find_packages

setup(
    name="DivaDivaModule",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'divadivamodule = divadivamodule:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['images/*', 'divadivamodule.py', 'modules_data.csv'],
    },
)
