==================
manga_down
===================

manga\_down is a tool to download manga from `Mangareader <https://www.mangareader.net>`__ and `Mangapanda <https://http://www.mangapanda.com>`__
-------------------------------------------------------------------------------------------------------------------------------------------------

\| green \| |Maintenance| |PyPI license| |Python >=3.6.9|

.. \|green\| image::
https://assets.readthedocs.org/static/projects/badges/passing-flat.svg

Installation
------------

::

    pip3 install manga_down

How to use?
-----------

Mangareader
~~~~~~~~~~~

To view all chapters available for manga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from manga_down import mangareader     #import mangareader from manga_down

    naruto = mangareader.Manga("naruto")   #initialize Manga class with manga name
    naruto.get_chapter_list()        #returns list of all chapters of given manga

Found the chapter number that you wanted to download?. Here's how to
download that chapter

.. code:: python

    naruto.download_chapter("120")  #just call the download_chapter by passing chapter number as argument

wanted to download the chapter in another folder?

::

    file_location = "/home/user/Downloads"
    naruto.download_chapter("120", file_location)#this will download the chapter in another folder passed as parameter 

--------------

Mangapanda
~~~~~~~~~~

To view all chapters available for manga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from manga_down import mangapanda   #import mangapanda from manga_down

    bleach = mangapanda.Manga("bleach")   #initialize Manga class with manga name
    bleach.get_chapter_list()        #returns list of all chapters of given manga

Found the chapter number that you wanted to download?. Here's how to
download that chapter

.. code:: python

    bleach.download_chapter("120")  #just call the download_chapter by passing chapter number as argument

wanted to download the chapter in another folder?

::

    file_location = "/home/user/Downloads"
    bleach.download_chapter("120", file_location)#this will download the chapter in another folder passed as parameter 

Found something unusual? Report `here <https://github.com/shaikhsajid1111/manga-down/issues>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LICENSE
-------

`MIT <LICENSE>`__

.. |Maintenance| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity
.. |PyPI license| image:: https://img.shields.io/pypi/l/ansicolortags.svg
   :target: https://pypi.python.org/pypi/ansicolortags/
.. |Python >=3.6.9| image:: https://img.shields.io/badge/python-3.6.9+-blue.svg
   :target: https://www.python.org/downloads/release/python-376/
