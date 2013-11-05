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
import webapp2 # for handlers
import os #for find dirname
from google.appengine.ext.webapp import template #for template render

class MainHandler(webapp2.RequestHandler):
    def get(self):   
        template_values = {}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'html/face.html')
        self.response.out.write(template.render(path, template_values))

class P1(webapp2.RequestHandler):
    def get(self):   
        template_values = {}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'html/P1.html')
        self.response.out.write(template.render(path, template_values))    

class D1(webapp2.RequestHandler):
    def get(self):   
        template_values = {}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'html/D1.html')
        self.response.out.write(template.render(path, template_values))      

  

    



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/P1', P1),
    ('/D1', D1)
], debug=True)
