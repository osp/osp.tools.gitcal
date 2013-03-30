#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of gitcal and is © the contributors, listed in README.txt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see http://www.gnu.org/licenses/.

Expects a visual culture style git api,
returns Ical Calendars of the commits
Dependency: vobject
"""

import json
from urllib2 import urlopen
from datetime import datetime

import vobject

from django.http import HttpResponse
from settings import API_PATH

def get_api(*args):
    url = API_PATH + '/'.join(args)
    res = urlopen(url)
    dict = json.loads(res.read())
    res.close
    return dict

def _render(repo_slug):
    repo = get_api(repo_slug)
    cal = vobject.iCalendar()
    
    print 'looking for', repo_slug
    print repo
    
    for commit in repo['commits']:
        vevent = cal.add('vevent')
        vevent.add('dtstart').value = datetime.fromtimestamp(commit['commit_time'])
        vevent.add('summary').value = "%s: %s" % (commit['author'], commit['message'])
        
    return cal.serialize()

def render(request, repo_slug):
    return HttpResponse(_render(repo_slug), mimetype="text/calendar")


