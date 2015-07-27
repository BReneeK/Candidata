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

The next line adds functions from a library
from HTMLParser import HTMLParser

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # embeds a video in the webpage
        self.response.write('''<iframe id=hilClint width="300" height="200" src=https://www.youtube.com/embed/6744Ym_5Ddg></iframe>
            <iframe id=benCarso width="300" height="200" src=https://www.youtube.com/embed/ulsA8aFOkRs></iframe>''')
# <iframe id=nameOfCand width="300" height="200" src=https://www.youtube.com/embed/IDofVid></iframe>

# IDs of videos of speeches where candidates are talking about issues they support
# jeb bush education jTWl3YoOXAc
# ben carson UN HHvFh6lSJqk
# chris cristie green energy uPxDnb2-aVI
# bobby jindal education nDCU-VlSgX0
# marco rubio military d9FVjcuz-pA
# rick santorum imigration 7Ruj9W9rufs
# 

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



        self.response.write(issues)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/clinton', ScrapingFromClintionHandler),
], debug=True)
