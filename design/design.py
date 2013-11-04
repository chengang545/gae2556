# -*- coding: utf-8 -*-
import cgi
import urllib
import wsgiref.handlers


from google.appengine.ext import db
from google.appengine.api import users
import webapp2

import os
from google.appengine.ext.webapp import template
from google.appengine.api import images



class Welcome(webapp2.RequestHandler):
    def get(self):
        title='制心一处，无事不办。'
        template_values = {
            'welcome': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'welcome.html')
        self.response.out.write(template.render(path, template_values))

    
class Poster0515(webapp2.RequestHandler):
    def get(self):
        title='Poster0515'
        template_values = {
            'poster0515': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'poster0515.html')
        self.response.out.write(template.render(path, template_values))

class Leena(webapp2.RequestHandler):
    def get(self):
        title='Leena'
        template_values = {
            'Leena': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'leena.html')
        self.response.out.write(template.render(path, template_values))
        
class Leki(webapp2.RequestHandler):
    def get(self):
        title='Leki'
        template_values = {
            'leki': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'leki.html')
        self.response.out.write(template.render(path, template_values))

class Document(webapp2.RequestHandler):
    def get(self):
        title='document picture model'
        template_values = {
            'document picture model': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Document Picture Model.html')
        self.response.out.write(template.render(path, template_values))

class Orgnization2013summer(webapp2.RequestHandler):
    def get(self):
        title='Orgnization2013summer'
        template_values = {
            'Orgnization2013summer': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'orgnization2013summer.html')
        self.response.out.write(template.render(path, template_values))

class LockerPhoto(webapp2.RequestHandler):
    def get(self):
        title='LockerPhoto'
        template_values = {
            'LockerPhoto': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'LockerPhoto.html')
        self.response.out.write(template.render(path, template_values))

class BabaOrdination(webapp2.RequestHandler):
    def get(self):
        title='BabaOrdination'
        template_values = {
            'BabaOrdination': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'BabaOrdination.html')
        self.response.out.write(template.render(path, template_values))

class BabaOrdinationEng(webapp2.RequestHandler):
    def get(self):
        title='BabaOrdinationEng'
        template_values = {
            'BabaOrdinationEng': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'BabaOrdinationEng.html')
        self.response.out.write(template.render(path, template_values))

class BabaOrdinationF(webapp2.RequestHandler):
    def get(self):
        title='BabaOrdinationF'
        template_values = {
            'BabaOrdinationF': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'BabaOrdinationF.html')
        self.response.out.write(template.render(path, template_values))


class BabaOrdinationBBMM(webapp2.RequestHandler):
    def get(self):
        title='BabaOrdinationBBMM'
        template_values = {
            'BabaOrdinationBBMM': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'BabaOrdinationBBMM.html')
        self.response.out.write(template.render(path, template_values))


class Forest2(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 2'
        template_values = {
            'Forest Sangha Newsletter 2': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 2.html')
        self.response.out.write(template.render(path, template_values))


class Transp(webapp2.RequestHandler):
    def get(self):
        title='Transp'

        mings=(
                'Phra Ronnapob Jotilabho',
                'Phra Sirimomgkhol Sirimongkalo',
                'Phra Pisit Jittasutdho',
                'Phra Aekarin Abhijāto',
                'Phra Narongchai Ṭhānajayo',
                'Phra Amnat Peetichayo',
                'Phra Samat Govito',
                'Phra Ruben Visālo',
                'Phra Elamale Sugatharathana',
                #'Phra Thai Oo Khemindo',
                #'Phra Kitipong Kittipiyo',
                #'Phra William Tejākaro',
                #'Phra Suriya Ṭhitakicco',
                #'Phra Preecha Ñāṇasotthiko',
                #'Phra Issarapap Yasindho',
                #'Phra Ruji Puṇṇacando',
                #'Phra Wee Lep Pavijjo',
                #'Phra Ou Qixing Kovido',
                'Phra Chen Gang Āsabho',
                'Phra Shakya Durga Raj Kittisakko',
                'Phra Leki Sangey Devo Dhanasabho',
                'Phra Daniel Lurie Dhammarko',
                'Phra Lai Chongrong Satindharo',
                'Phra Li Baoyong Ñāṇindo',
                'Phra Tan Tengyew Pabhāsaro',
                'Phra Yeung Siukei Ñānuttamo',
                'Phra Upendra Manapo',
                'Phra Wei Feihu Adhidhammo',
                'Phra Hao Botang Manindo',
                'Phra Todd Naovaransy Suddhōbhāsō',
                'Phra Dhiman Barua Aggavijjō',
                'Phra Ronald Sanvoravong Guṇavarō',
                'Phra Mongsapru Chowdhury Manuññō',
                'Phra Bimal Assam Ātapō',
                'Phra Ching Thoyai Marma Sēṭṭhapaññō',
                'Phra Tanapoom Tejapongvorachai Surajayō',
                'Phra Sayni Barua Attārakkhō',
                'Phra Chatchawan Chuleekeit Guṇajōtō',
                'Phra Garison Chakma Paguṇō',
                'Phra Mongshinu Mogh Kantapaññō',
                'Phra Wong Jiun Shin Cirasubhō',
                'Phra Liu Dan Dantamanō',
                'Phra Liu Dan Dantamanō',
                'Phra Phra Hung Chiu Fung',
                'Phra Phra Hu Junqiao')
               

        template_values = {
            'transp': title,
            'mings': mings
        }

        

        path = os.path.join(os.path.dirname(__file__), 'transp.html')
        self.response.out.write(template.render(path, template_values))



class Thaialpha(webapp2.RequestHandler):
    def get(self):
        title='Transp'
        mings=(
            (('ก','k'),('ข(ฃ)','kh')),
            (('ค(ฅ)','g'),('ฆ','gh')),
            (('จ','c'),('ฉ','ch')),
            (('ช','j'),('ฌ','jh')),
            (('ต','t'),('ด','th')),
            (('ฏ','t'),('ถ','th')),
            (('ฎ','ṭ'),('ฐ','ṭh')),
            (('ท','d'),('ธ','dh-')),
            (('ฑ','ḍ'),('ฒ','ḍh')),
            (('ป','b(p)'),('บภ','bh')),
            (('พ','p(b)'),('ผ','ph')),
            (('ฟ','f'),('ฝ','fh')),          
            (('ฮ','o'),('อ','oh')),
            (('ฬ','h(ḷ)'),('ห','hh')),
            (('ล','l'),('ร','lh(r)')),
            (('ม','m'),('ว','v')),
            (('น','n'),('ณ','ṇ')),
            (('ย','y'),('ญ','ñ')),
            (('ซ','s'),('ศษส','sh')),
            (('-ํ','ṁ'),('ง','g')),

            )              
        template_values = {'transp': title,'mings': mings}
        path = os.path.join(os.path.dirname(__file__), 'thaialpha.html')
        self.response.out.write(template.render(path, template_values))

class Forest1(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 1'
        template_values = {
            'Forest Sangha Newsletter 1': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 1.html')
        self.response.out.write(template.render(path, template_values))


class Forest2(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 2'
        template_values = {
            'Forest Sangha Newsletter 2': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 2.html')
        self.response.out.write(template.render(path, template_values))

class Forest3(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 3'
        template_values = {
            'Forest Sangha Newsletter 3': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 3.html')
        self.response.out.write(template.render(path, template_values))


class Forest4(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 4'
        template_values = {
            'Forest Sangha Newsletter 4': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 4.html')
        self.response.out.write(template.render(path, template_values))


class Forest5(webapp2.RequestHandler):
    def get(self):
        title='Forest Sangha Newsletter 5'
        template_values = {
            'Forest Sangha Newsletter 5': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'Forest Sangha Newsletter 5.html')
        self.response.out.write(template.render(path, template_values))


class Idopinfopaper(webapp2.RequestHandler):
    def get(self):
        title='IDOP Info Paper'
        template_values = {
            'IDOP Info Paper': title,
        }
        path = os.path.join(os.path.dirname(__file__), 'idopinfo.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/poster0515',Poster0515),
    ('/leena',Leena),
    ('/leki',Leki),
    ('/document picture model',Document),
    ('/orgnization2013summer',Orgnization2013summer),
    ('/LockerPhoto',LockerPhoto),
    ('/BabaOrdination',BabaOrdination),
    ('/BabaOrdinationEng',BabaOrdinationEng),
    ('/BabaOrdinationF',BabaOrdinationF),
    ('/BabaOrdinationBBMM',BabaOrdinationBBMM),
    ('/transp',Transp),
    ('/thaialpha',Thaialpha),
    ('/Forest Sangha Newsletter 1',Forest1),
    ('/Forest Sangha Newsletter 2',Forest2),
    ('/Forest Sangha Newsletter 3',Forest3),
    ('/Forest Sangha Newsletter 4',Forest4),
    ('/Forest Sangha Newsletter 5',Forest5),
    ('/idopinfo',Idopinfopaper)
], debug=True)


def main():
    application.RUN()


if __name__ == '__main__':
    main()
    
