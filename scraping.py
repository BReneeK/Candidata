import webapp2
#!/usr/bin/env python
import os
import jinja2
from google.appengine.api import urlfetch
import htmlentities

# from lxml import html
# import requests

# The next line adds functions from a library
from HTMLParser import HTMLParser
# from html.entities import name2codepoint


        #
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

# '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
#              '"http://www.ontheissues.org/Hillary_Clinton.htm">')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Leelabari')
        issues = []
        # page is the website in html
        # page = requests.get('http://www.ontheissues.org/Hillary_Clinton.htm')
        # tree is the html in string formats
        # tree = html.fromstring(page.text)

        # issues.extend(issue_about_abortion)
        # self.response.write(issues)
        #

        parser.feed('<html><head><title>Test</title></head>'
                    '<body><h1>Parse me!</h1></body></html>')

        self.response.write(parser.feed)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/clinton', ScrapingFromClintionHandler)
], debug=True)
