from setuptools import setup

setup(name='Inserta Logo',
    version='0.0.1',
    description='Proyecto IV-DAI',
    url='https://github.com/magvugr',
    author='Miguel Angel Garcia Villegas',
    author_email='magvugr@gmail.com',
    license='GNU General Public License',
    packages=['insertaLogo'],
    install_requires=[
        'django',
        'wheel',
    ],
    zip_safe=False)