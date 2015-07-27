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
import os
import jinja2
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
import json

jinja_environment = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Candidate(ndb.Model):
    name = ndb.StringProperty(required=True)
    party = ndb.StringProperty(required=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        self.response.write('Hello world!')
        issues = []
        #
=======
        candidate_id = self.request.get('id')
        if not candidate_id:
            template = jinja_environment.get_template('templates/index.html')
            self.response.write(template.render())
            #candidate_id = self.request.get('id')
            for candidate in Candidate.query().fetch():
                self.response.write(candidate.name + ", " + candidate.party + '<br>')

        else:
            candidate_key = ndb.Key(Candidate, int(candidate_id))
            candidate = candidate_key.get()


            template = jinja_environment.get_template('templates/index.html')
            self.response.write(template.render({
            'name': candidate.name,
            'party': candidate.party,
            }))

class AddHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/add.html')
        self.response.write(template.render())

        h_clinton = Candidate(name = "Hillary Clinton", party = "Democrat")
        l_chafee = Candidate(name = "Lincoln Chafee", party = "Democrat")
        m_omalley = Candidate(name = "Martin O'Malley", party = "Democrat")
        b_sanders = Candidate(name = "Bernie Sanders", party = "Democrat")
        j_webb = Candidate(name = "Jim Webb", party = "Democrat")
        j_bush = Candidate(name = "Jeb Bush", party = "Republican")
        b_carson = Candidate(name = "Ben Carson", party = "Republican")
        c_christie = Candidate(name = "Chris Christie", party = "Republican")
        t_cruz = Candidate(name = "Ted Cruz", party = "Republican")
        c_fiorina = Candidate(name = "Carly Fiorina", party = "Republican")
        l_graham = Candidate(name = "Lindsey Graham", party = "Republican")
        m_huckabee = Candidate(name = "Mike Huckabee", party = "Republican")
        b_jindal = Candidate(name = "Bobby Jindal", party = "Republican")
        j_kasich = Candidate(name = "John Kasich", party = "Republican")
        g_pataki = Candidate(name = "George Pataki", party = "Republican")
        r_paul = Candidate(name = "Rand Paul", party = "Republican")
        r_perry = Candidate(name = "Rick Perry", party = "Republican")
        m_rubio = Candidate(name = "Marco Rubio", party = "Repiblican")
        r_santorum = Candidate(name = "Rick Santorum", party = "Republican")
        d_trump = Candidate(name = "Donald Trump", party = "Republican")
        s_walker = Candidate(name = "Scott Walker", party = "Republican")

        candidates = [h_clinton, l_chafee, m_omalley, b_sanders, j_webb, j_bush, b_carson, c_christie,
        t_cruz, c_fiorina, l_graham, m_huckabee, b_jindal, j_kasich, g_pataki, r_paul, r_perry,
        m_rubio, r_santorum, d_trump, s_walker]

        for person in candidates:
            person.put()

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/search.html')

        search = self.request.get("search")
        result = Candidate.query(Candidate.name == search).get()

        self.response.write(template.render({
        'result': result,
        'search': search
        }))

class LinkHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/links.html')

        search = self.request.get("search")
        result = Candidate.query(Candidate.name == search).get()

        self.response.write(template.render({
        'result': result,
        'search': search
        }))
>>>>>>> 51e59e965260d0cf6a74878dd1c23b90ad11a0a3

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/search', SearchHandler),
    ('/links', LinkHandler),
], debug=True)
