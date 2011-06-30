from setuptools import setup
from setuptools import find_packages
import os

setup(
    name='django-shop-configurableproduct',
    version='0.2.5',
    packages=find_packages(),
    install_requires=[
        'sorl-thumbnail',
        'django-shop',
    ],
    author='Pavel Zhukov',
    author_email='gelios@gmail.com',
    description='Configurable product for django-shop',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    license='GPL',
    keywords='django-shop, product',
    url='http://bitbucket.org/zeus/configurableproduct',
    include_package_data=True,
)

