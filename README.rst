=======================
plonetheme.aqueouslight
=======================


Introduction
============

*plonetheme.aqueouslight* Theme is an installable Plone_ Theme using the **theming** and **packaging** 
features available in `plone.app.theming`_ to make `Aqueous Light`_ theme by `Six Shooter Media`_ easly available in `Plone`.

.. image:: https://github.com/collective/plonetheme.aqueouslight/raw/master/plonetheme/aqueouslight/static/preview.png

Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Zipfile
-------

If you are an **end user**, you might enjoy installation via zip file import.

1. Download the `zip file <https://github.com/collective/plonetheme.aqueouslight/raw/master/aqueouslight.zip>`_.
2. Import the theme from the Diazo theme control panel.


Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.aqueouslight`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.aqueouslight


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.aqueouslight',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` on ``Plonetheme Redmusic`` theme from the Diazo control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/collective/plonetheme.aqueouslight/issues
- Source Code: https://github.com/collective/plonetheme.aqueouslight


License
=======

This package is licensed under the GPL Version 2.


Credits
-------

- Sebastian Kalinowski ``sebastian.kalinowski@stxnext.pl``.
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).


Contact
=======

.. image:: http://stxnext.pl/open-source/files/stx-next-logo

**STX Next** Sp. z o.o.

- http://stxnext.pl

- info@stxnext.pl


.. _`Plone`: http://plone.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Aqueous Light`: http://www.sixshootermedia.com/ostemplates/aqueous_light
.. _`Six Shooter Media`: http://www.sixshootermedia.com/
.. _`Diazo`: http://diazo.org
