import webapp2
#!/usr/bin/env python
import os
import jinja2
from google.appengine.api import urlfetch
import htmlentities
from html.entities import name2codepoint

# from lxml import html
# import requests

# The next line adds functions from a library
from HTMLParser import HTMLParser
# from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("End tag  :", tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment  :", data)
    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)
    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)
    # def handle_decl(self, data):
    #     print("Decl     :", data)


# instantiate the parser and fed it some HTML
issues = []

f = open('inputclinton.html')
contentclinton = f.read()

parser = MyHTMLParser()
parser.feed(contentclinton)





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
