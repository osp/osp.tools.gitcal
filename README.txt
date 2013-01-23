**********
OSP GitCal
**********

Create an iCalendar file based on the commits in a git repository.

Django:
=======

In settings.py, add ``gitcal`` to your ``INSTALLED_APPS``. Add a variabele
``API_PATH`` set to the web-reachable address of a git_info API (as provided
by `OSP Visual Culture <http://osp.constantvzw.org/tools/visualculture/>`_).

For example:

``API_PATH = 'http://ospwork.constantvzw.org/api/'``

As a python module
==================

You can import the function ``_render`` from ``gitcal``. It takes as
arguments the name of the repository, and the path to the git api, and
returns the text of the icalendar.

Requirements
============

`vobject <http://vobject.skyhouseconsulting.com/>`_

License
=======

Copyright (C) 2013 Eric Schrijver
for OSP Open Source Publishing

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see http://www.gnu.org/licenses/.


