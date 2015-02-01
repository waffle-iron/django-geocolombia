=====
Django-Geocolombia
=====

Django-Geocolombia is a simple Django app to deal with cities and states in Colombia. It currently supports codes and names of Colombian States and Cities.

Installation
-----------

Download from PyPi
::

    $ pip install django-geocolombia
    
Or download dist folder from GitHub repository.
::

    $ pip install dist/django-geocolombia-0.1.zip
    
Add "geocolombia" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'geocolombia',
    )

Usage
-----------

You need to import geocolombia models at the top of your views. The app provides the following models and attributes:

* ``State`` – code, name.
* ``City`` – code, name.

Example
-----------

::

    $ from geocolombia.models import *
    $ State.objects.all().count()
    $ => 32
    $ State.objects.get(name='Norte de Santander')
    $ => <State: 54 Norte de Santander>
    $ State.objects.get(name='Norte de Santander').cities()
    $ => [<City: 54001 C├â┬║cuta>, <City: 54003 ├â┬übrego>, <City: 54051 Arboledas>, <City: 54099 Bochalema>, <City: 54109 Bucarasica>, <City: 54125 C├ícota>, <City: 54128 C├íchira>, <City: 54172 Chin├ícota>, <City: 54174 Chitag├í>, <City: 54206 Convenci├│n>, <City: 54223 Cucutilla>, <City: 54239 Durania>, <City: 54245 El Carmen>, <City: 54250 El Tarra>, <City: 54261 El Zulia>, <City: 54313 Gramalote>, <City: 54344 Hacar├¡>, <City: 54347 Herr├ín>, <City: 54377 Labateca>, <City: 54385La Esperanza>, '...(remaining elements truncated)...']

Contributing
-----------

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

