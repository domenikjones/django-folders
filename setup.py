from setuptools import setup, find_packages

setup(
    name="django-folders",
    author="Jonas und der Wolf GmbH",
    author_email="info@jonasundderwolf.de",
    version='0.1',
    packages=find_packages(),
    install_requires=['django-spurl'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
