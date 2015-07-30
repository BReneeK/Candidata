
#!/usr/bin/env python
# coding: utf-8
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
import sys
import jinja2
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch
import logging
import json
import re
from operator import eq

# intID2# from html.entities import name2codepoint


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Candidate(ndb.Model):

    name = ndb.StringProperty(required =True)
    website = ndb.StringProperty(required =True)

    party = ndb.StringProperty(required =True)
    bio = ndb.StringProperty(required =True)

    abortion = ndb.StringProperty(required =True)
    marriage = ndb.StringProperty(required =True)
    aff_action = ndb.StringProperty(required =True)
    env_reg = ndb.StringProperty(required =True)
    deny_service = ndb.StringProperty(required =True)
    net_neutrality = ndb.StringProperty(required = True)
    corp_tax = ndb.StringProperty(required = True)
    prog_tax = ndb.StringProperty(required = True)
    health_care = ndb.StringProperty(required =True)
    border_sec = ndb.StringProperty(required = True)
    army_spend = ndb.StringProperty(required = True)
    isis = ndb.StringProperty(required = True)

    intID1 = ndb.StringProperty(required = True)
    intID2 = ndb.StringProperty(required = True)
    speID1 = ndb.StringProperty(required = True)
    speID2 = ndb.StringProperty(required = True)



class User(ndb.Model):
    name = ndb.StringProperty(required = True)
    abortion = ndb.StringProperty(required = True)
    marriage = ndb.StringProperty(required = True)
    aff_action = ndb.StringProperty(required = True)
    env_reg = ndb.StringProperty(required = True)
    deny_service = ndb.StringProperty(required = True)
    net_neutrality = ndb.StringProperty(required = True)
    corp_tax = ndb.StringProperty(required = True)
    prog_tax = ndb.StringProperty(required = True)
    health_care = ndb.StringProperty(required = True)
    border_sec = ndb.StringProperty(required = True)
    army_spend = ndb.StringProperty(required = True)
    isis = ndb.StringProperty(required = True)



class MainHandler(webapp2.RequestHandler):
    def get(self):

#        googleUser = users.get_current_user()
#        userGoogleID = googleUser.user_id()

#        newUser = User(id = userGoogleID)
#        newUser.put()

        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

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

        bios = {

            "HC": "Hillary Diane Rodham Clinton (born October 26, 1947) is an American politician. She was United States Secretary of State in the administration of President Barack Obama from 2009 to 2013, a United States Senator representing New York from 2001 to 2009, and, as the wife of President Bill Clinton, First Lady of the United States from 1993 to 2001. A leading candidate for the Democratic Party's nomination to the 2008 presidential election, she has announced her candidacy for the Democratic nomination in the 2016 presidential election.",
            "LD": "Lincoln Davenport Chafee (born March 26, 1953) is an American politician from Rhode Island who has served as the Mayor of Warwick (1993-1999), a U.S. Senator (1999-2007) and as the 74th Governor of Rhode Island (2011-2015).",
            "MM": "Martin Joseph O'Malley (born January 18, 1963) is an American politician who served as the 61st Governor of Maryland, from 2007 to 2015. Prior to being elected as Governor, he served as the Mayor of Baltimore from 1999 to 2007, having previously served as a Baltimore City Councilor from 1991 to 1999. A member of the Democratic Party, he served as the Chair of the Democratic Governors Association from 2011 to 2013. Following his departure from public office in early 2015, he was appointed to the Johns Hopkins University's Carey Business School as a visiting professor focusing on government, business, and urban issues.",
            "BS": "Bernard 'Bernie' Sanders (born September 8, 1941) is an American politician and the junior United States Senator from Vermont. He has announced his candidacy for the Democratic nomination in the 2016 presidential election. Sanders is the longest-serving independent in U.S. congressional history. A self-described democratic socialist, he favors policies similar to those of social democratic parties in Europe, particularly those of Scandinavia.He caucuses with the Democratic Party and has been the ranking minority member on the Senate Budget Committee since January 2015.",
            "JW": "James Henry 'Jim' Webb, Jr. (born February 9, 1946) is an American politician and author. He has served as a United States Senator from Virginia, Secretary of the Navy, Assistant Secretary of Defense, Counsel for the House Veterans Affairs Committee, and Marine Corps officer. In the private sector he has been an Emmy-award winning journalist, a filmmaker, and the author of ten books. In addition, he taught literature at the United States Naval Academy and was a Fellow at the Harvard Institute of Politics. As a member of the Democratic Party, Webb announced on November 19, 2014, that he was forming an exploratory committee to evaluate a run for President of the United States in 2016. On July 2, 2015, he announced that he would be joining the race for the Democratic nomination for President.",
            "JB": "John Ellis 'Jeb' Bush (born February 11, 1953) is an American businessman and politician who served as the 43rd Governor of Florida from 1999 to 2007. He is the second son of former President George H. W. Bush and former First Lady Barbara Bush, and the younger brother of former President George W. Bush.",
            "BC": "Benjamin Solomon 'Ben' Carson, Sr. (born September 18, 1951) is an American politician, author, and retired Johns Hopkins neurosurgeon. He was the first surgeon to successfully separate conjoined twins joined at the head. In 2008, he was awarded the Presidential Medal of Freedom by President George W. Bush. After delivering a widely publicized speech at the 2013 National Prayer Breakfast, he became a popular conservative figure in political media for his views on social and political issues. Carson is running for the Republican nomination for President of the United States in the 2016 election.",
            "CC": "Christopher James 'Chris' Christie (born September 6, 1962) is an American politician and member of the Republican Party who has served as the 55th Governor of New Jersey since January 2010.",
            "TC": "Rafael Edward 'Ted' Cruz (born December 22, 1970) is the junior United States Senator from Texas. Elected in 2012 as a Republican, he is the first Hispanic or Cuban American to serve as a U.S. Senator from Texas. He is the chairman of the subcommittee on the Oversight, Agency Action, Federal Rights and Federal Courts, U.S. Senate Judiciary Committee. He is also the chairman of the United States Senate Commerce Subcommittee on Space, Science and Competitiveness, U.S. Senate Commerce Committee.",
            "CF": "Cara Carleton 'Carly' Fiorina (born September 6, 1954) is an American politician, former business executive, and current chair of the non-profit organization Good360. Starting in 1980, Fiorina rose through the ranks to become an executive at AT&T and its equipment and technology spinoff, Lucent. As chief executive officer of Hewlett-Packard (HP) from 1999 to 2005, she was the first woman to lead one of the top twenty U.S. companies.",
            "LG": "Lindsey Olin Graham (born July 9, 1955) is an American politician and member of the Republican Party, who has served as a United States Senator from South Carolina since 2003, and has been the senior Senator from South Carolina since 2005. On June 1, 2015, he announced his candidacy for the Presidency of the United States in the 2016 election.",
            "MH": "Michael Dale 'Mike' Huckabee (born August 24, 1955) is an American author and politician who served as the 44th Governor of Arkansas from 1996 to 2007. He was a candidate in the 2008 United States Republican presidential primaries. He won the 2008 Iowa Republican caucuses and finished second in delegate count and third in both popular vote and number of states won, behind nominee John McCain and Mitt Romney.",
            "BJ": "Piyush 'Bobby' Jindal (born June 10, 1971) is an American politician who is the 55th and current governor of Louisiana and the former vice chairman of the Republican Governors Association. In 1996, Governor Murphy Foster appointed Jindal secretary of the Louisiana Department of Health and Hospitals, and in 1999 he was appointed president of the University of Louisiana System. In 2001, Jindal was appointed as the principal adviser to Tommy Thompson, the United States Secretary of Health and Human Services by the 43rd President, George W. Bush.",
            "JK": "John Richard Kasich (born May 13, 1952) is an American politician who has served as the 69th Governor of Ohio since 2011. He is also a candidate for the Republican Party\'s nomination to the 2016 presidential election. Kasich served as a member of the United States House of Representatives, representing Ohio's 12th congressional district from 1983 to 2001. He was a commentator on Fox News Channel, hosting Heartland with John Kasich (2001-2007). He also worked as an investment banker, as managing director of Lehman Brothers' Columbus, Ohio office until the firm collapsed in 2008.",
            "GP": "George Elmer Pataki (born June 24, 1945) is an American lawyer and politician who served as the 53rd Governor of New York (1995-2006). A member of the Republican Party, Pataki was a lawyer who was elected Mayor of his home town of Peekskill, later going on to be elected to State Assembly, then State Senate. In 1994, he ran for Governor against three-term incumbent Mario Cuomo, defeating him by over a three-point margin as part of the Republican Revolution of 1994. Pataki, succeeding a three-term Governor, would himself be elected to three consecutive terms, and was one of only three Republican governors of New York elected since 1923, the others being Thomas Dewey and Nelson Rockefeller.",
            "RPa": "Dr. Randal Howard 'Rand' Paul (born January 7, 1963) is an American politician and physician. Since 2011, Paul has served in the United States Senate as a member of the Republican Party representing Kentucky. He is the son of former U.S. Representative Ron Paul of Texas.",
            "RPe": "James Richard 'Rick' Perry (born March 4, 1950) is an American politician who served as the 47th Governor of Texas from 2000 to 2015. A Republican, he was elected Lieutenant Governor of Texas in 1998 and assumed the governorship in December 2000 when then-governor George W. Bush resigned to become President of the United States. Perry is the longest serving governor in Texas state history. As a result, he is the only governor in modern Texas history to have appointed at least one person to every eligible state office, board, or commission position (as well as to several elected offices to which the governor can appoint someone to fill an unexpired term, such as six of the nine current members of the Texas Supreme Court).",
            "MR": "Marco Antonio Rubio (born May 28, 1971) is the junior United States Senator from Florida, serving since January 2011. A member of the Republican Party, he previously served as Speaker of the Florida House of Representatives.",
            "RS": "Richard John 'Rick' Santorum (born May 10, 1958) is an American attorney and Republican Party politician. He served as a United States Senator representing Pennsylvania (1995-2007) and was the Senate\'s third-ranking Republican (2001-07). He ran as a candidate for the 2012 Republican Party presidential nomination, finishing second to the eventual Republican nominee Mitt Romney.",
            "DT": "Donald John Trump (born June 14, 1946) is an American business magnate, investor, television personality, and author. He is the chairman and president of The Trump Organization and the founder of Trump Entertainment Resorts. Trump's lifestyle and outspoken manner, as well as his books and his media appearances, have made him an American celebrity. He hosted The Apprentice, a US TV show. On June 16, 2015 at Trump Tower in Manhattan, Trump formally announced his candidacy for President of the United States in the 2016 election, seeking the nomination of the Republican Party.",
            "SW": "Scott Kevin Walker (born November 2, 1967) is an American politician and the 45th Governor of Wisconsin, serving since 2011. Walker is also a candidate for the Republican Party's nomination to the 2016 presidential election. Walker served in the Wisconsin State Assembly and as the Milwaukee County Executive before his election as governor in 2010. He survived a 2012 recall election and was reelected governor in 2014, defeating Democrat Mary Burke."
        }


        h_clinton = Candidate(name = "Hillary Clinton", party = "Democrat", website = "http://www.ontheissues.org/Hillary_Clinton.htm", bio = bios["HC"], intID1 = "7XOoOgsj_z8", intID2 = "cYKwU2MwI-8", speID1 = "6744Ym_5Ddg", speID2 = "Q4O8xo9EWb8",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        l_chafee = Candidate(name = "Lincoln Chafee", party = "Democrat", website = "http://www.ontheissues.org/Lincoln_Chafee.htm", bio = bios["LD"], intID1 = "IVpF6_qpfq4", intID2 = "9XobXVbqhZg", speID1 = "XEMwtaMSox4", speID2 = "XhM4-kjFqRI",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        m_omalley = Candidate(name = "Martin O'Malley", party = "Democrat", website = "http://www.ontheissues.org/Martin_O%60Malley.htm", bio = bios["MM"], intID1 = "Qod0dsZythc", intID2 = "HOiMPIJ2xEw", speID1 = "4cte1kH_7BQ", speID2 = "kIsgYAYfst8",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        b_sanders = Candidate(name = "Bernie Sanders", party = "Democrat", website = "http://www.ontheissues.org/Bernie_Sanders.htm", bio = bios["BS"], intID1 = "XpgJYNaIeqo", intID2 = "S5vOKKMipSA", speID1 = "0zHSW2k-vF0", speID2 = "fL12Gb_ixtU",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        j_webb = Candidate(name = "Jim Webb", party = "Democrat", website = "http://www.ontheissues.org/Jim_Webb.htm", bio = bios["JW"], intID1 = "4606giVTfM0", intID2 = "F1qNdqt1VTE", speID1 = "sdvrHh0iRtU", speID2 = "n6vEWeGJU54",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        j_bush = Candidate(name = "Jeb Bush", party = "Republican", website = "http://www.ontheissues.org/Jeb_Bush.htm", bio = bios["JB"], intID1 = "5DBwlicegzI", intID2 = "7edfSVLhA_8", speID1 = "jTWl3YoOXAc", speID2 = "pxBIsMz5cZ0",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        b_carson = Candidate(name = "Ben Carson", party = "Republican", website = "http://www.ontheissues.org/Ben_Carson.htm", bio = bios["BC"], intID1 = "iGoZkJ8T_ic", intID2 = "h1269Q6J8LA", speID1 = "HHvFh6lSJqk", speID2 = "AD2Q4tReN3k",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        c_christie = Candidate(name = "Chris Christie", party = "Republican", website = "http://www.ontheissues.org/Chris_Christie.htm", bio = bios["CC"], intID1 = "C-yGeUSNttw", intID2 = "da4T9CKfnqQ", speID1 = "uPxDnb2-aVI", speID2 = "P4-gVP78t9s",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        t_cruz = Candidate(name = "Ted Cruz", party = "Republican", website = "http://www.ontheissues.org/Ted_Cruz.htm", bio = bios["TC"], intID1 = "1gq2mJHndk4", intID2 = "SZRFVU1y7LE", speID1 = "kkeC53P9rVI", speID2 = "0YurHI-d3Dk",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        c_fiorina = Candidate(name = "Carly Fiorina", party = "Republican", website = "http://www.ontheissues.org/Carly_Fiorina.htm", bio = bios["CF"], intID1 = "8yhl509cp98", intID2 = "A8b-tOYJhho", speID1 = "tiFegTYmyK0", speID2 = "ygeS92QiqPk",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        l_graham = Candidate(name = "Lindsey Graham", party = "Republican", website = "http://www.ontheissues.org/Lindsey_Graham.htm", bio = bios["LG"], intID1 = "vTbpiDseuoE", intID2 = "7oYspOu5dBs", speID1 = "YQtRPhkUKRw", speID2 = "Ifqu2BXCwgc",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        m_huckabee = Candidate(name = "Mike Huckabee", party = "Republican", website = "http://www.ontheissues.org/Mike_Huckabee.htm", bio = bios["MH"], intID1 = "PmokmskIqDU", intID2 = "qckb860gXqY", speID1 = "000uvNgzVrA", speID2 = "yaW-iyzFrN4",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        b_jindal = Candidate(name = "Bobby Jindal", party = "Republican", website = "http://www.ontheissues.org/Bobby_Jindal.htm", bio = bios["BJ"], intID1 = "crHzzwNgtno", intID2 = "_WWN4Zc_pz4", speID1 = "nDCU-VlSgX0", speID2 = "g7dopUHX6RE",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        j_kasich = Candidate(name = "John Kasich", party = "Republican", website = "http://www.ontheissues.org/John_Kasich.htm", bio = bios["JK"], intID1 = "lTWTGOcgXQw", intID2 = "yuAUUnFVdVQ", speID1 = "cOHiWQ6A9Io", speID2 = "epvFuEYMDcc",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        g_pataki = Candidate(name = "George Pataki", party = "Republican", website = "http://www.ontheissues.org/George_Pataki.htm", bio = bios["GP"], intID1 = "eV9IwbVL48g", intID2 = "A-XxCyzqgNQ", speID1 = "F6hoj6Ycpvo", speID2 = "gWVgXGvP27U",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        r_paul = Candidate(name = "Rand Paul", party = "Republican", website = "http://www.ontheissues.org/Rand_Paul.htm", bio = bios["RPa"], intID1 = "WFLmJXv9890", intID2 = "5S13zAMc3aQ", speID1 = "O0sE_jh9HQU", speID2 = "dE08GKNlU60",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        r_perry = Candidate(name = "Rick Perry", party = "Republican", website = "http://www.ontheissues.org/Rick_Perry.htm", bio = bios["RPe"], intID1 = "5H77JCfYcxc", intID2 = "PMNs3yaeWhE", speID1 = "-xOu_o0ugg0", speID2 = "m94nWv0jawk",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        m_rubio = Candidate(name = "Marco Rubio", party = "Republican", website = "http://www.ontheissues.org/Marco_Rubio.htm", bio = bios["MR"], intID1 = "W0YB0fhhFYI", intID2 = "GkbSzX4Zum0", speID1 = "d9FVjcuz-pA", speID2 = "3AUZ5w7NKoA",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        r_santorum = Candidate(name = "Rick Santorum", party = "Republican", website = "http://www.ontheissues.org/Rick_Santorum.htm", bio = bios["RS"], intID1 = "ZVzUDIlMS-o", intID2 = "P6HwFiHvJMk", speID1 = "sJB6TVfz8-E", speID2 = "_pL6JyvwPN0",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")
        d_trump = Candidate(name = "Donald Trump", party = "Republican", website = "http://www.ontheissues.org/Donald_Trump.htm", bio = bios["DT"], intID1 = "AJNfbthf9GA", intID2 = "4dyngfj6kAY", speID1 = "kj9xsrhJKOQ", speID2 = "qXjz3qLufv8",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False", corp_tax = "False", prog_tax = "False", health_care = "False",
            border_sec = "False", army_spend = "False", isis = "False")
        s_walker = Candidate(name = "Scott Walker", party = "Republican", website = "http://www.ontheissues.org/Scott_Walker.htm", bio = bios["SW"], intID1 = "Ju1s_AgO4EA", intID2 = "MTwxgNYHwUA", speID1 = "tmra5Xp_T10", speID2 = "livagJq8_aU",
            abortion = "False", marriage = "False", aff_action = "False", env_reg = "False", deny_service = "False", net_neutrality = "False",
            corp_tax = "False", prog_tax = "False", health_care = "False", border_sec = "False", army_spend = "False", isis = "False")

        # intID1 is the ID for the first Interview video
        # speID1 is the ID for the first Speech video

        candidates = [h_clinton, l_chafee, m_omalley, b_sanders, j_webb, j_bush, b_carson, c_christie,
        t_cruz, c_fiorina, l_graham, m_huckabee, b_jindal, j_kasich, g_pataki, r_paul, r_perry,
        m_rubio, r_santorum, d_trump, s_walker]


        for person in candidates:
            url = person.website
            url_file = urlfetch.fetch(url)
            url_html = url_file.content

            abortion_response2 = re.search(r'<b>\s+<a name=\'q1\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if abortion_response2:
                strippedverion = abortion_response2.group(1).replace(" ", "").strip()
                logging.info(strippedverion)
                if strippedverion == "StronglyFavors" or strippedverion == "Favors":
                    person.abortion = "True"
                    logging.info("has worked")
                else:
                    person.abortion = "False"
                    logging.info(person.abortion)
                    logging.info("fail")

            else:
                person.abortion = "False"

            marriage_response = re.search(r'<b>\s+<a name=\'q3\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if marriage_response:
                strippedverion1 = marriage_response.group(1).replace(" ", "").strip()
                if strippedverion1 == "StronglyFavors" or strippedverion1 == "Favors":
                    person.marriage = "True"
                else:
                    person.marriage = "False"
            else:
                person.marriage = "False"

            deny_service_response = re.search(r'Ok to deny services', url_html, re.MULTILINE)
            if deny_service_response:
                person.deny_service = "True"
            else:
                person.deny_service = "False"

            aff_action_response = re.search(r'<b>\s+<a name=\'q2\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if aff_action_response:
                strippedversion2 = aff_action_response.group(1).replace(" ", "").strip()
                if strippedversion2 == "Favors" or strippedversion2 == "StronglyFavors":
                    person.aff_action = "True"
                else:
                    person.aff_action = "False"
            else:
                person.aff_action = "False"

            env_reg_response= re.search(r'<b>\s+<a name=\'q8\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if env_reg_response:
                strippedverion3 = env_reg_response.group(1).replace(" ", "").strip()
                if strippedverion3 == "Favors" or strippedversion2 == "StronglyFavors":
                    person.env_reg = "True"
                else:
                    person.env_reg = "False"
            else:
                person.env_reg = "False"

            net_neutrality_response = re.search(r'Voted NO on establishing \"network neutrality\"', url_html, re.MULTILINE)
            if net_neutrality_response:
                person.net_neutrality = "False"
            net_neutrality_response = re.search(r'Ensure net neutrality', url_html, re.MULTILINE)
            if net_neutrality_response:
                person.net_neutrality = "True"

            prog_tax_response = re.search(r'<b>\s+<a name=\'q11\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if prog_tax_response:
                strippedverion4 = prog_tax_response.group(1).replace(" ", "").strip()
                if strippedverion4 == "StronglyFavors" or strippedverion4 == "Favors":
                    person.prog_tax = "True"
                else:
                    person.prog_tax = "False"
            else:
                person.prog_tax = "False"

            health_care_response = re.search(r'<b>\s+<a name=\'q5\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if health_care_response:
                strippedversion5 = health_care_response.group(1).replace(" ", "").strip()
                if strippedversion5 == "StronglyFavors" or strippedversion5 == "Favors":
                    person.health_care = "True"
                else:
                    person.health_care = "False"
            else:
                person.health_care = "False"

            border_sec_response = re.search(r'More border patrolling | Secure border', url_html, re.MULTILINE)
            if border_sec_response:
                person.border_sec = "True"
            else:
                person.border_sec = "False"

            border_sec_response2 = re.search(r'NO on building a fence along the Mexican border', url_html, re.MULTILINE)
            if border_sec_response:
                person.border_sec = "False"

            army_spend_response = re.search(r'<b>\s+<a name=\'q15\'></a>\s+(.*)\n</b>', url_html, re.MULTILINE)
            if army_spend_response:
                strippedversion6 = army_spend_response.group(1).replace(" ", "").strip()
                if strippedversion6 == "StronglyFavors" or strippedversion6 == "Favors":
                    person.army_spend = "True"
                else:
                    person.army_spend = "False"
            else:
                person.army_spend = "False"

            isis_response = re.search(r'need strategy against ISIS', url_html, re.MULTILINE)
            if isis_response:
                person.isis = "True"
            else:
                person.isis = "False"

            corp_tax_response = re.search(r'Cutting taxes on job creators | cut taxes on businesses', url_html, re.MULTILINE)
            if corp_tax_response:
                person.corp_tax = "False"
            else:
                person.corp_tax = "True"

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

        print result.website

        url_file = urlfetch.fetch(result.website)
        url_html = url_file.content


        self.response.write(template.render({
        'result': result,
        'search': search,
        }))

class CandidateHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/candidates.html')

        candidate1 = Candidate.get_by_id(int(self.request.get('candidate')))
        logging.info(candidate1)



        self.response.write(template.render({
            'candidate1': candidate1,
            'abortion': candidate1.abortion,
            'marriage' : candidate1.marriage,
            'aff_action' : candidate1.aff_action,
            'env_reg' : candidate1.env_reg,
            'deny_service' : candidate1.deny_service,
            'net_neutrality' : candidate1.net_neutrality,
            'corp_tax' : candidate1.corp_tax,
            'prog_tax' : candidate1.prog_tax,
            'health_care' : candidate1.health_care,
            'border_sec' : candidate1.border_sec,
            'army_spend' : candidate1.army_spend,
            'isis' : candidate1.isis

        }))

class UserHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()

        if user:
            greeting = ('Welcome, %s!(<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        (users.create_login_url('/profile')))
        # user.put()

        self.response.out.write('<html><body>%s</body></html>' % greeting)
        self.response.write(template.render())

class FormHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/questions.html')
        self.response.write(template.render())

class AnswerHandler(webapp2.RequestHandler):
    def post(self):
        template = jinja_environment.get_template('templates/answers.html')

        name = self.request.get('name')
        abortion = self.request.get('abortion')
        marriage = self.request.get('marriage')
        aff_action = self.request.get('aff_action')
        env_reg = self.request.get('env_reg')
        deny_service = self.request.get('deny_service')
        net_neutrality = self.request.get('net_neutrality')
        corp_tax = self.request.get('corp_tax')
        prog_tax = self.request.get('prog_tax')
        health_care = self.request.get('health_care')
        border_sec = self.request.get('border_sec')
        army_spend = self.request.get('army_spend')
        isis = self.request.get('isis')

        user = User(name = name, abortion = eval(abortion), marriage = eval(marriage), aff_action = eval(aff_action), env_reg = eval(env_reg), deny_service = eval(deny_service), net_neutrality = eval(net_neutrality),
        corp_tax = eval(corp_tax), prog_tax = eval(prog_tax), health_care = eval(health_care), border_sec = eval(border_sec), army_spend = eval(army_spend), isis = eval(isis))

        #currUser = users.get_current_user()
#        currID = currUser.user_id()
#        user = User.get_by_id(currID)

#        user.abortion = abortion
#        user.marriage = marriage
#        user.aff_action = aff_action
#        user.env_reg = env_reg
#        user.deny_service = deny_service
#        user.net_neutrality = net_neutrality
#        user.corp_tax = corp_tax
#        user.prog_tax = prog_tax
#        user.health_care = health_care
#        user.border_sec = border_sec
#        user.army_spend = army_spend
#        user.isis = isis
#        user.put()

        user_key = user.put()

        id = user_key.id()

        self.response.write(template.render(
        {
            'abortion' : abortion,
            'marriage' : marriage,
            'aff_action' : aff_action,
            'env_reg' : env_reg,
            'deny_service' : deny_service,
            'net_neutrality' : net_neutrality,
            'corp_tax' : corp_tax,
            'prog_tax' : prog_tax,
            'health_care' : health_care,
            'border_sec' : border_sec,
            'army_spend' : army_spend,
            'isis' : isis

        }
        ))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/profile.html')

        name = self.request.get('name')
        abortion = self.request.get('abortion')
        marriage = self.request.get('marriage')
        aff_action = self.request.get('aff_action')
        env_reg = self.request.get('env_reg')
        deny_service = self.request.get('deny_service')
        net_neutrality = self.request.get('net_neutrality')
        corp_tax = self.request.get('corp_tax')
        prog_tax = self.request.get('prog_tax')
        health_care = self.request.get('health_care')
        border_sec = self.request.get('border_sec')
        army_spend = self.request.get('army_spend')
        isis = self.request.get('isis')


        # user = User(name = name, abortion = abortion, marriage = marriage, aff_action = aff_action, env_reg = env_reg, deny_service = deny_service, net_neutrality = net_neutrality, corp_tax = corp_tax, prog_tax = prog_tax, health_care = health_care, border_sec = border_sec, army_spend = army_spend, isis = isis)
        '''currUser = users.get_current_user()
            currID = currUser.user_id()
            user = User.get_by_id(currID)

            user.abortion = abortion
            user.marriage = marriage
            user.aff_action = aff_action
            user.env_reg = env_reg
            user.deny_service = deny_service
            user.net_neutrality = net_neutrality
            user.corp_tax = corp_tax
            user.prog_tax = prog_tax
            user.health_care = health_care
            user.border_sec = border_sec
            user.army_spend = army_spend
            user.isis = isis
            user.put()
'''


        user_key = user.put()

        id = user_key.id()

        candidates = []

        for person in Candidate.query():
            candidates.append(person)

        similarities = []
        total = 0
        your_candidates = []

        for candidate in candidates:

            candidate_issues = [candidate.abortion, candidate.marriage, candidate.aff_action, candidate.env_reg, candidate.deny_service, candidate.net_neutrality, candidate.corp_tax, candidate.prog_tax, candidate.health_care, candidate.border_sec, candidate.army_spend, candidate.isis]
            user_issues = [user.abortion, user.marriage, user.aff_action, user.env_reg, user.deny_service, user.net_neutrality, user.corp_tax, user.prog_tax, user.health_care, user.border_sec, user.army_spend, user.isis]

            for num in range(0,len(candidate_issues)):
                if candidate_issues[num] == user_issues[num]:
                    total+=1
            if total>0:
                your_candidates.append(candidate)

            similarities.append(total)
            total = 0

        similarities.sort(reverse = True)

        the_range = range(len(your_candidates))


        self.response.write(template.render(
        {
            'name' : name,
            'abortion' : abortion,
            'marriage' : marriage,
            'aff_action' : aff_action,
            'env_reg' : env_reg,
            'deny_service' : deny_service,
            'net_neutrality' : net_neutrality,
            'corp_tax' : corp_tax,
            'prog_tax' : prog_tax,
            'health_care' : health_care,
            'border_sec' : border_sec,
            'army_spend' : army_spend,
            'isis' : isis,
            'similarities' : similarities,
            'your_candidates': your_candidates,
            'candidates': candidates,
            'the_range': the_range,
            'isis' : isis

            }
            ))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/search', SearchHandler),
    ('/links', LinkHandler),
    ('/candidates', CandidateHandler),
    ('/login', UserHandler),
    ('/questions', FormHandler),
    ('/answers', AnswerHandler),
    ('/profile', ProfileHandler)

], debug=True)
