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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''<iframe id=vid1 width="300" height="200" src=https://www.youtube.com/embed/6744Ym_5Ddg frameborder="0"></iframe>
            <iframe id=vid1 width="300" height="200" src=https://www.youtube.com/embed/ulsA8aFOkRs frameborder="0"></iframe>''')
# jeb bush education jTWl3YoOXAc
# ben carson UN HHvFh6lSJqk
# chris cristie green energy uPxDnb2-aVI
#
#

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
