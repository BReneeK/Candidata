#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
#!/usr/bin/env python
import os
import jinja2

from lxml import html
import requests

# The next line adds functions from a library
from HTMLParser import HTMLParser

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class ScrapingFromClintionHandler(webapp2.RequestHandler):
    def get(self):
        issues = []
        # page is the website in html
        page = requests.get('http://www.ontheissues.org/default.htm')
        # tree is the html in string formats
        tree = html.fromstring(page.text)

        #This will create a list of buyers:
        # issues = tree.xpath('//div[@title="buyer-name"]/text()')

        #This will create a list of prices

        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')
        issue_about_abortion = tree.xpath('//id[@class="abortion"]/text()')



        issues.extend(issue_about_abortion, )
        self.response.write(issues)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/clinton', ScrapingFromClintionHandler)
], debug=True)
