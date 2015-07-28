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
from google.appengine.api import urlfetch
import json
<<<<<<< HEAD
import logging

logger = logging.getLogger()
=======
# from html.entities import name2codepoint
from HTMLParser import HTMLParser
>>>>>>> b925ef03f52b0ea68d79a6b7a86d43f3e77364bd

jinja_environment = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Candidate(ndb.Model):
    name = ndb.StringProperty(required=True)
    party = ndb.StringProperty(required=True)
    website = ndb.StringProperty(required = False)

<<<<<<< HEAD
=======




>>>>>>> b925ef03f52b0ea68d79a6b7a86d43f3e77364bd
class MainHandler(webapp2.RequestHandler):
    def get(self):


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

        h_clinton = Candidate(name = "Hillary Clinton", party = "Democrat", website = "http://www.ontheissues.org/Hillary_Clinton.htm")
        l_chafee = Candidate(name = "Lincoln Chafee", party = "Democrat", website = "http://www.ontheissues.org/Lincoln_Chafee.htm")
        m_omalley = Candidate(name = "Martin O'Malley", party = "Democrat", website = "http://www.ontheissues.org/Martin_O%60Malley.htm")
        b_sanders = Candidate(name = "Bernie Sanders", party = "Democrat", website = "http://www.ontheissues.org/Bernie_Sanders.htm")
        j_webb = Candidate(name = "Jim Webb", party = "Democrat", website = "http://www.ontheissues.org/Jim_Webb.htm")
        j_bush = Candidate(name = "Jeb Bush", party = "Republican", website = "http://www.ontheissues.org/Jeb_Bush.htm")
        b_carson = Candidate(name = "Ben Carson", party = "Republican", website = "http://www.ontheissues.org/Ben_Carson.htm")
        c_christie = Candidate(name = "Chris Christie", party = "Republican", website = "http://www.ontheissues.org/Chris_Christie.htm")
        t_cruz = Candidate(name = "Ted Cruz", party = "Republican", website = "http://www.ontheissues.org/Ted_Cruz.htm")
        c_fiorina = Candidate(name = "Carly Fiorina", party = "Republican", website = "http://www.ontheissues.org/Carly_Fiorina.htm")
        l_graham = Candidate(name = "Lindsey Graham", party = "Republican", website = "http://www.ontheissues.org/Lindsey_Graham.htm")
        m_huckabee = Candidate(name = "Mike Huckabee", party = "Republican", website = "http://www.ontheissues.org/Mike_Huckabee.htm")
        b_jindal = Candidate(name = "Bobby Jindal", party = "Republican", website = "http://www.ontheissues.org/Bobby_Jindal.htm")
        j_kasich = Candidate(name = "John Kasich", party = "Republican", website = "http://www.ontheissues.org/John_Kasich.htm")
        g_pataki = Candidate(name = "George Pataki", party = "Republican", website = "http://www.ontheissues.org/George_Pataki.htm")
        r_paul = Candidate(name = "Rand Paul", party = "Republican", website = "http://www.ontheissues.org/Rand_Paul.htm")
        r_perry = Candidate(name = "Rick Perry", party = "Republican", website = "http://www.ontheissues.org/Rick_Perry.htm")
        m_rubio = Candidate(name = "Marco Rubio", party = "Repiblican", website = "http://www.ontheissues.org/Marco_Rubio.htm")
        r_santorum = Candidate(name = "Rick Santorum", party = "Republican", website = "http://www.ontheissues.org/Rick_Santorum.htm")
        d_trump = Candidate(name = "Donald Trump", party = "Republican", website = "http://www.ontheissues.org/Donald_Trump.htm")
        s_walker = Candidate(name = "Scott Walker", party = "Republican", website = "http://www.ontheissues.org/Scott_Walker.htm")

        candidates = [h_clinton, l_chafee, m_omalley, b_sanders, j_webb, j_bush, b_carson, c_christie,
        t_cruz, c_fiorina, l_graham, m_huckabee, b_jindal, j_kasich, g_pataki, r_paul, r_perry,
        m_rubio, r_santorum, d_trump, s_walker]

        for person in candidates:
            person.put()

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/search.html')

        search = self.request.get("search")

        self.response.write(template.render({
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

<<<<<<< HEAD
class CandidateHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/candidates.html')

        candidate = Candidate.get_by_id(int(self.request.get('candidate')))

        #candidate_id = result.Key()
        #candidate = Candidate.get_by_id(int(candidate_id))

        #self.response.write(result.name)

        self.response.write(template.render({
        'candidate': candidate,
        }))
=======


>>>>>>> b925ef03f52b0ea68d79a6b7a86d43f3e77364bd

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/search', SearchHandler),
    ('/links', LinkHandler),
<<<<<<< HEAD
    ('/candidates', CandidateHandler)
=======
    ('/s_walker', )
>>>>>>> b925ef03f52b0ea68d79a6b7a86d43f3e77364bd
], debug=True)
