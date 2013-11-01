from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open(os.path.join('docs', 'HISTORY.txt')).read()
    )

setup(name='plonetheme.aqueouslight',
      version=version,
      description="An installable Diazo theme for Plone 4.1",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='web python plone diazo theme',
      author='STX Next Sp. z o.o, Sebastian Kalinowski',
      author_email='info@stxnext.pl',
      url='https://github.com/collective/plonetheme.aqueouslight',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
