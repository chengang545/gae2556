import cgi
import urllib
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import os
from google.appengine.ext.webapp import template
from google.appengine.api import images
import datetime


#welcome homepage
class Face(webapp2.RequestHandler):
    def get(self):   
        template_values = {}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'face.html')
        self.response.out.write(template.render(path, template_values))

# Modle for every IDOP Member
class IdopMember(db.Model):
    #Part 1: Personal Information
    nameen = db.StringProperty(multiline=True)
    nameth = db.StringProperty(multiline=True)
    monknameen = db.StringProperty(multiline=True)
    monknameth = db.StringProperty(multiline=True)
    ordinationdate = db.StringProperty()
    ordination_place = db.StringProperty()
    #Nationality
    countryarea = db.StringProperty(multiline=True)
    #ethnicity_race
    nationrace = db.StringProperty()
    religion = db.StringProperty() 
    nativelanguage = db.StringProperty()
    second_language = db.StringProperty()
    otherlanguage = db.StringProperty(multiline=True)
    place_of_birth = db.StringProperty()
    registered_permanent_residence = db.StringProperty() 
    birthday = db.StringProperty()
    height = db.StringProperty()
    weight = db.StringProperty()
    skincolor = db.StringProperty()
    tatto = db.TextProperty()
    scar = db.TextProperty()
    #previous occupation
    occupation = db.StringProperty()
    maritalstatus = db.StringProperty()
    fathername = db.StringProperty()
    father_nationality = db.StringProperty()
    father_birthday = db.StringProperty()
    mothername = db.StringProperty()
    mother_nationality = db.StringProperty()
    mother_birthday = db.StringProperty()  

    #Part 2: Contact Information 
    email = db.StringProperty()
    #Mobile Phone (In Thailand) 
    mobilphone = db.StringProperty()
    current_home_address = db.StringProperty(multiline=True)
    home_city = db.StringProperty()
    home_state = db.StringProperty()
    home_country = db.StringProperty()
    home_zip_code = db.StringProperty()
    home_phone = db.StringProperty()
    name_of_emergency_person = db.StringProperty() 
    relationship_with_emergency_person = db.StringProperty() 
    emergency_person_home_address = db.StringProperty(multiline=True)
    emergency_person_city = db.StringProperty()
    emergency_person_state = db.StringProperty()
    emergency_person_country = db.StringProperty()
    emergency_person_zip_code = db.StringProperty()
    emergencyphone = db.StringProperty()
    emergency_person_email = db.StringProperty()

    #Part 3: Educational Information 
    #Highest Educational Level Completed 
    education = db.TextProperty()
    highest_education_year_of_completion = db.StringProperty()
    highest_education_major = db.StringProperty()
    highest_education_institution_name = db.TextProperty()
    highest_education_country = db.StringProperty()
    #other education
    other_education = db.TextProperty()
    other_education_year_of_completion = db.StringProperty()
    other_education_major = db.StringProperty()
    other_education_institution_name = db.TextProperty()
    other_education_country = db.StringProperty()

    #Part 4: Thailand Entry Information 
    passport_number = db.StringProperty()
    passport_issue_date = db.StringProperty()
    passport_expiration_date = db.StringProperty()

    #Part 5: Photo
    photo = db.BlobProperty()
    passport = db.BlobProperty()

    inout = db.StringProperty()
    
    
    
    
    
    
    
    
    
#show basic infornation of Idopmembers    
class MemberInfo(webapp2.RequestHandler):
    def get(self):
        idopmembers = IdopMember.all().filter("inout =","Residein").order('ordinationdate').order('birthday').fetch(200)
        #if "ordination" is save as db.Text it's not in index so and not gql or ordered
        #change to "unicode" for index and unicode.
        # orderd by 'ordinationdate' then orderd by 'birthday' for same 'ordinationdate'.
        template_values = {'idopmembers': idopmembers,}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'info.html')
        self.response.out.write(template.render(path, template_values))

#show details of Idopmembers    
class Detail(webapp2.RequestHandler):
    def get(self):        
        w = db.get(self.request.get("detail_id"))       
        template_values = {'w': w,}
        path = os.path.join(os.path.dirname(__file__), 'detail.html')
        self.response.out.write(template.render(path, template_values))


#for show photo Image
class Image(webapp2.RequestHandler):
    def get(self):
        m = db.get(self.request.get("img_id"))
        if m.photo:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(m.photo)

#for show Passport image
class Passport(webapp2.RequestHandler):
    def get(self):
        n = db.get(self.request.get("passport_id"))
        if n.passport:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(n.passport)

#for batabase admin CRUD
class Admin(webapp2.RequestHandler):
    def get(self):
        idopmembers = IdopMember.all().order('ordinationdate').order('birthday').fetch(200)    
        template_values = {'idopmembers': idopmembers,}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'Check.html')
        self.response.out.write(template.render(path, template_values))

#create
class Add(webapp2.RequestHandler):
    def get(self):
        title='Plus'
        template_values = {'add': title,}
        path = os.path.join(os.path.dirname(__file__), 'add.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        idopmember = IdopMember()
        idopmember.nameen = self.request.get('nameen')
        idopmember.nameth = self.request.get('nameth')
        idopmember.monknameen = self.request.get('monknameen')
        idopmember.monknameth = self.request.get('monknameth')     
        idopmember.ordinationdate = self.request.get('ordinationdate')
        idopmember.ordination_place = self.request.get('ordination_place')
        idopmember.countryarea = self.request.get('countryarea') 
        #ethnicity_race  
        idopmember.nationrace = self.request.get('nationrace')   
        idopmember.religion = self.request.get('religion')   
        idopmember.nativelanguage = self.request.get('nativelanguage')
        idopmember.second_language = self.request.get('second_language')
        idopmember.otherlanguage = self.request.get('otherlanguage')
        idopmember.place_of_birth = self.request.get('place_of_birth')
        idopmember.registered_permanent_residence = self.request.get('registered_permanent_residence')
        idopmember.birthday = self.request.get('birthday')
        idopmember.height = self.request.get('height')
        idopmember.weight = self.request.get('weight')
        idopmember.skincolor = self.request.get('skincolor')
        idopmember.tatto = self.request.get('tatto')
        idopmember.scar = self.request.get('scar')     
        #previous occupation
        idopmember.occupation = self.request.get('occupation')
        idopmember.maritalstatus = self.request.get('maritalstatus')
        idopmember.fathername = self.request.get('fathername')
        idopmember.father_nationality = self.request.get('father_nationality')
        idopmember.father_birthday = self.request.get('father_birthday')
        idopmember.mothername = self.request.get('mothername')
        idopmember.mother_nationality = self.request.get('mother_nationality')
        idopmember.mother_birthday = self.request.get('mother_birthday')
        #Part 2: Contact Information 
        idopmember.email = self.request.get('email')
        #Mobile Phone (In Thailand) 
        idopmember.mobilphone = self.request.get('mobilphone')
        idopmember.current_home_address = self.request.get('current_home_address')
        idopmember.home_city = self.request.get('home_city')
        idopmember.home_state = self.request.get('home_state')
        idopmember.home_country = self.request.get('home_country')
        idopmember.home_zip_code = self.request.get('home_zip_code')
        idopmember.home_phone = self.request.get('home_phone')
        idopmember.name_of_emergency_person = self.request.get('name_of_emergency_person')
        idopmember.relationship_with_emergency_person = self.request.get('relationship_with_emergency_person')
        idopmember.emergency_person_home_address = self.request.get('emergency_person_home_address')
        idopmember.emergency_person_city = self.request.get('emergency_person_city')
        idopmember.emergency_person_state = self.request.get('emergency_person_state')
        idopmember.emergency_person_country = self.request.get('emergency_person_country')
        idopmember.emergency_person_zip_code = self.request.get('emergency_person_zip_code')
        idopmember.emergencyphone = self.request.get('emergencyphone')
        idopmember.emergency_person_email = self.request.get('emergency_person_email')
        #Part 3: Educational Information 
        #Highest Educational Level Completed 
        idopmember.education = self.request.get('education')
        idopmember.highest_education_year_of_completion = self.request.get('highest_education_year_of_completion')
        idopmember.highest_education_major = self.request.get('highest_education_major')
        idopmember.highest_education_institution_name = self.request.get('highest_education_institution_name')
        idopmember.highest_education_country = self.request.get('highest_education_country')
        idopmember.other_education = self.request.get('other_education')
        idopmember.other_education_year_of_completion = self.request.get('other_education_year_of_completion')
        idopmember.other_education_major = self.request.get('other_education_major')
        idopmember.other_education_institution_name = self.request.get('other_education_institution_name')
        idopmember.other_education_country = self.request.get('other_education_country') 
        #Part 4: Thailand Entry Information 
        idopmember.passport_number = self.request.get('passport_number')
        idopmember.passport_issue_date = self.request.get('passport_issue_date')
        idopmember.passport_expiration_date = self.request.get('passport_expiration_date')  
        #Part 5: Photo
        idopmember.photo = self.request.get('photo')
        idopmember.passport = self.request.get('passport')  

        inout = self.request.get('inout')   

        idopmember.put()
        self.redirect('/admin')

#update
class Change(webapp2.RequestHandler):
    def get(self):
        v = db.get(self.request.get("change_id"))
        template_values = {'v': v,}
        path = os.path.join(os.path.dirname(__file__), 'change.html')
        self.response.out.write(template.render(path, template_values))
    def post(self): 
        upnameen = self.request.get('nameen')
        upnameth = self.request.get('nameth')
        upmonknameen = self.request.get('monknameen')
        upmonknameth = self.request.get('monknameth')     
        upordinationdate = self.request.get('ordinationdate')
        upordination_place = self.request.get('ordination_place')
        upcountryarea = self.request.get('countryarea') 
        #ethnicity_race  
        upnationrace = self.request.get('nationrace')   
        upreligion = self.request.get('religion')   
        upnativelanguage = self.request.get('nativelanguage')
        upsecond_language = self.request.get('second_language')
        upotherlanguage = self.request.get('otherlanguage')
        upplace_of_birth = self.request.get('place_of_birth')
        upregistered_permanent_residence = self.request.get('registered_permanent_residence')
        upbirthday = self.request.get('birthday')
        upheight = self.request.get('height')
        upweight = self.request.get('weight')
        upskincolor = self.request.get('skincolor')
        uptatto = self.request.get('tatto')
        upscar = self.request.get('scar')     
        #previous occupation
        upoccupation = self.request.get('occupation')
        upmaritalstatus = self.request.get('maritalstatus')
        upfathername = self.request.get('fathername')
        upfather_nationality = self.request.get('father_nationality')
        upfather_birthday = self.request.get('father_birthday')
        upmothername = self.request.get('mothername')
        upmother_nationality = self.request.get('mother_nationality')
        upmother_birthday = self.request.get('mother_birthday')
        #Part 2: Contact Information 
        upemail = self.request.get('email')
        #Mobile Phone (In Thailand) 
        upmobilphone = self.request.get('mobilphone')
        upcurrent_home_address = self.request.get('current_home_address')
        uphome_city = self.request.get('home_city')
        uphome_state = self.request.get('home_state')
        uphome_country = self.request.get('home_country')
        uphome_zip_code = self.request.get('home_zip_code')
        uphome_phone = self.request.get('home_phone')
        upname_of_emergency_person = self.request.get('name_of_emergency_person')
        uprelationship_with_emergency_person = self.request.get('relationship_with_emergency_person')
        upemergency_person_home_address = self.request.get('emergency_person_home_address')
        upemergency_person_city = self.request.get('emergency_person_city')
        upemergency_person_state = self.request.get('emergency_person_state')
        upemergency_person_country = self.request.get('emergency_person_country')
        upemergency_person_zip_code = self.request.get('emergency_person_zip_code')
        upemergencyphone = self.request.get('emergencyphone')
        upemergency_person_email = self.request.get('emergency_person_email')
        #Part 3: Educational Information 
        #Highest Educational Level Completed 
        upeducation = self.request.get('education')
        uphighest_education_year_of_completion = self.request.get('highest_education_year_of_completion')
        uphighest_education_major = self.request.get('highest_education_major')
        uphighest_education_institution_name = self.request.get('highest_education_institution_name')
        uphighest_education_country = self.request.get('highest_education_country')
        upother_education = self.request.get('other_education')
        upother_education_year_of_completion = self.request.get('other_education_year_of_completion')
        upother_education_major = self.request.get('other_education_major')
        upother_education_institution_name = self.request.get('other_education_institution_name')
        upother_education_country = self.request.get('other_education_country')
        #Part 4: Thailand Entry Information 
        uppassport_number = self.request.get('passport_number')
        uppassport_issue_date = self.request.get('passport_issue_date')
        uppassport_expiration_date = self.request.get('passport_expiration_date')
        #Part 5: Photo
        #upphoto = self.request.get('photo')
        #uppassport = self.request.get('passport')     
        upinout = self.request.get('inout')    



        v = db.get(self.request.get('id'))
        v.nameen =  unicode(upnameen)# unicode for "no-Ascii codecs string"
        v.nameen = unicode(upnameen)
        v.nameth = unicode(upnameth)
        v.monknameen = unicode(upmonknameen)
        v.monknameth = unicode(upmonknameth)     
        v.ordinationdate = unicode(upordinationdate)
        v.ordination_place = unicode(upordination_place)
        v.countryarea = unicode(upcountryarea) 
        #ethnicity_race  
        v.nationrace = unicode(upnationrace)   
        v.religion = unicode(upreligion)   
        v.nativelanguage = unicode(upnativelanguage)
        v.second_language = unicode(upsecond_language)
        v.otherlanguage = unicode(upotherlanguage)
        v.place_of_birth = unicode(upplace_of_birth)
        v.registered_permanent_residence = unicode(upregistered_permanent_residence)
        v.birthday = unicode(upbirthday)
        v.height = unicode(upheight)
        v.weight = unicode(upweight)
        v.skincolor = unicode(upskincolor)
        v.tatto = db.Text(uptatto)
        v.scar = db.Text(upscar)     
        #previous occupation
        v.occupation = unicode(upoccupation)
        v.maritalstatus = unicode(upmaritalstatus)
        v.fathername = unicode(upfathername)
        v.father_nationality = unicode(upfather_nationality)
        v.father_birthday = unicode(upfather_birthday)
        v.mothername = unicode(upmothername)
        v.mother_nationality = unicode(upmother_nationality)
        v.mother_birthday = unicode(upmother_birthday)
        #Part 2: Contact Information 
        v.email = unicode(upemail)
        #Mobile Phone (In Thailand) 
        v.mobilphone = unicode(upmobilphone)
        v.current_home_address = unicode(upcurrent_home_address)
        v.home_city = unicode(uphome_city)
        v.home_state = unicode(uphome_state)
        v.home_country = unicode(uphome_country)
        v.home_zip_code = unicode(uphome_zip_code)
        v.home_phone = unicode(uphome_phone)
        v.name_of_emergency_person = unicode(upname_of_emergency_person)
        v.relationship_with_emergency_person = unicode(uprelationship_with_emergency_person)
        v.emergency_person_home_address = unicode(upemergency_person_home_address)
        v.emergency_person_city = unicode(upemergency_person_city)
        v.emergency_person_state = unicode(upemergency_person_state)
        v.emergency_person_country = unicode(upemergency_person_country)
        v.emergency_person_zip_code = unicode(upemergency_person_zip_code)
        v.emergencyphone = unicode(upemergencyphone)
        v.emergency_person_email = unicode(upemergency_person_email)
        #Part 3: Educational Information 
        #Highest Educational Level Completed 
        v.education = db.Text(upeducation)
        v.highest_education_year_of_completion = unicode(uphighest_education_year_of_completion)
        v.highest_education_major = unicode(uphighest_education_major)
        v.highest_education_institution_name = db.Text(uphighest_education_institution_name)
        v.highest_education_country = unicode(uphighest_education_country)
        v.other_education =db.Text(upother_education)
        v.other_education_year_of_completion = unicode(upother_education_year_of_completion)
        v.other_education_major = unicode(upother_education_major)
        v.other_education_institution_name = db.Text(upother_education_institution_name)
        v.other_education_country = unicode(upother_education_country)   
        #Part 4: Thailand Entry Information 
        v.passport_number = unicode(uppassport_number)
        v.passport_issue_date = unicode(uppassport_issue_date)
        v.passport_expiration_date = unicode(uppassport_expiration_date)  
        #Part 5: Photo
        #v.photo = unicode(upphoto)
        #v.passport = unicode(uppassport)   
        v.inout = unicode(upinout)
        v.put()
        self.redirect('/admin')

#update photo(beacuse if in changinfo page, it will receive a nill so destroy the original image, same with property "passport")
class Changephoto(webapp2.RequestHandler):
    def get(self):
        v = db.get(self.request.get("changephoto_id"))     
        template_values = {'v': v,}
        path = os.path.join(os.path.dirname(__file__), 'changephoto.html')
        self.response.out.write(template.render(path, template_values))
    def post(self): 
        upphoto = self.request.get('photo')  
        v = db.get(self.request.get("id"))
        v.photo = db.Blob(upphoto)  
        v.put()
        self.redirect('/admin')

#update passport
class Changepassport(webapp2.RequestHandler):
    def get(self):
        v = db.get(self.request.get("changepassport_id"))
        template_values = {'v': v,}
        path = os.path.join(os.path.dirname(__file__), 'changepassport.html')
        self.response.out.write(template.render(path, template_values))
    def post(self): 
        uppassport = self.request.get('passport')  
        v = db.get(self.request.get("id"))
        v.passport = db.Blob(uppassport)       
        v.put()
        self.redirect('/admin')

#delete
class Delete(webapp2.RequestHandler):
    def get(self):
        v = db.get(self.request.get("delete_id"))    
        template_values = {"v":v,}
        path = os.path.join(os.path.dirname(__file__), 'delete.html')
        self.response.out.write(template.render(path, template_values))
    def post(self): 
        v = db.get(self.request.get('id'))
        v.delete()
        self.redirect('/admin')

#for contacks list
class Contacts(webapp2.RequestHandler):
    def get(self):
        persons = IdopMember.all().filter("inout =","Residein").order('ordinationdate').order('birthday').fetch(200)
        template_values = {'persons': persons,}
        path = os.path.join(os.path.dirname(__file__), 'contacts.html')
        self.response.out.write(template.render(path, template_values))


#for download photo
class DownPhoto(webapp2.RequestHandler):
    def get(self):
        idopmembers = IdopMember.all().filter("inout =","Residein").order('ordinationdate').order('birthday').fetch(200)    
        template_values = {'idopmembers': idopmembers,}#can be easy 
        path = os.path.join(os.path.dirname(__file__), 'photo.html')
        self.response.out.write(template.render(path, template_values))

#for download passport
class DownPassport(webapp2.RequestHandler):
    def get(self):
        idopmembers_query = IdopMember.all().filter("inout =","Residein").order('ordinationdate').order('birthday')
        idopmembers = idopmembers_query.fetch(200)
        template_values = {'idopmembers': idopmembers,}
        path = os.path.join(os.path.dirname(__file__), 'passport.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
    ('/', Face),
    ('/info', MemberInfo),
    ('/img', Image),
    ('/passport', Passport),
    ('/detail',Detail),
    ('/admin',Admin),
    ('/add', Add),
    ('/change', Change),
    ('/changephoto', Changephoto),
    ('/changepassport', Changepassport),
    ('/delete',Delete),
    ("/contacts",Contacts),
    ("/downphoto",DownPhoto),
    ("/downpassport",DownPassport),
], debug=True)


def main():
    application.RUN()


if __name__ == '__main__':
    main()
    
