from flask import Flask ,request,render_template,url_for
from flask_wtf import form
from flask_mongoengine import MongoEngine

db=MongoEngine()
app=Flask(__name__)

app.config['MONGODB-SETTINGS']={
'db':'abc',
'host':'mongodb://localhost:27017/abc'
}
db.init_app(app)

class Company(db.Document):

   name=db.StringField(unique=True)
   license_number=db.StringField()
   formation_year=db.StringField()
   location=db.StringField()
   ceoname=db.StringField()
   companyemailid=db.StringField()
   mobilenumber=db.IntField()
   numberofproducts=db.StringField()
@app.route('/')
def x():
  y= Company(name='Allusion',formation_year='2015',location='kphb',ceoname='sravani',companyemailid='sravani66@gmail.com',mobilenumber='9701118651',numberofproducts='25')
  y.save()
  return Company.objects().to_json()

if __name__ == '__main__':
     app.run(debug=True)
