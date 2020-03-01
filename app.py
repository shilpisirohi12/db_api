import flask
import json
from flask import request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app =flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://cutr:cutr@127.0.0.1:3306/world'
db=SQLAlchemy(app)


class WorldData(db.Model):
    __tablename__='city'
    id=db.Column('ID', db.INT, primary_key=True)
    name=db.Column('Name',db.CHAR(35))
    country_code=db.Column('CountryCode',db.CHAR(3))
    district=db.Column('District',db.CHAR(20))
    population=db.Column('Population',db.INT)



    def __repr__(self):
        return self.id



@app.route('/', methods=['GET'])
def initPoint():
    return render_template('home.html')

@app.route("/api/v1/resources/city/all", methods=['GET'])
def api_AllData():
    cities=WorldData.query.all()
    cityList=[]
    """"Creating List Of Distionaries"""
    for city in cities:
        cityList.append({'id':city.id,'name':city.name,'country_code':city.country_code,'district':city.district,'population':city.population})
        #print(city.id,city.name,city.country_code,city.district,city.population)
    #print(cityList)
    return jsonify(cityList)

@app.route("/api/v1/resources/city", methods=['GET'])
def api_byID():
    results=[]    
    if 'name' in request.args:
        name=request.args['name']
        cityData=WorldData.query.filter(WorldData.name==name).all()
        cityList=[]
        for city in cityData:
            cityList.append({'id':city.id,'name':city.name,'country_code':city.country_code,'district':city.district,'population':city.population})

    else:
        return " No city name found in request URL. Please enter URL with parameter name"
 

    return jsonify(cityList)

if __name__ == "__main__":
    app.run(debug=True)