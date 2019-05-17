import os
from flask import Flask
from flask import render_template, request, redirect, url_for
import requests

from flask_sqlalchemy import SQLAlchemy

project_dir= os.path.dirname(os.path.abspath(__file__))
database_file='sqlite:///{}'.format(os.path.join(project_dir, 'weather.db' ))

app=Flask(__name__)
db=SQLAlchemy(app)

class User(db.Model):
    username=db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password=db.Column(db.String(80), nullable=True)

    def __rep__(self):
        return "User:<{}>".format(self.username)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/weather", methods=['post'])
def weather():
    city=request.form['city_name']
    r=requests.get('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&mode=json&appid=e0fc2d0b038108cd17f1b71026ece2ce')
    json_object = r.json()
    data_descr = {
    'Country':json_object['city']['country'],
    'City':json_object['city']['name'],
    'City_id':json_object['city']['id'],
    }

    """
    Day 1
    Dict holding weather forecast values for day 1.
    """
    day1_pred={
    'Date':json_object['list'][6]['dt_txt'].split(' ')[0],
    'day1_morning':{
    'Temperature': str(round(float(json_object['list'][6]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][6]['main']['pressure'],
    'Humidity':json_object['list'][6]['main']['humidity'],
    'Description':json_object['list'][6]['weather'][0]['description'],
    'Icon':json_object['list'][6]['weather'][0]['icon'],
    'Time': json_object['list'][6]['dt_txt'].split(' ')[1]
    },
    'day1_noon':{
    'Temperature': str(round(float(json_object['list'][7]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][7]['main']['pressure'],
    'Humidity':json_object['list'][7]['main']['humidity'],
    'Description':json_object['list'][7]['weather'][0]['description'],
    'Icon':json_object['list'][7]['weather'][0]['icon'],
    'Time': json_object['list'][7]['dt_txt'].split(' ')[1]
    },
    'day1_evening': {
    'Temperature': str(round(float(json_object['list'][9]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][9]['main']['pressure'],
    'Humidity':json_object['list'][9]['main']['humidity'],
    'Description':json_object['list'][9]['weather'][0]['description'],
    'Icon':json_object['list'][9]['weather'][0]['icon'],
    'Time': json_object['list'][9]['dt_txt'].split(' ')[1]
    },
    }
    """
    DAY 2
    """
    day2_pred={
    'Date':json_object['list'][13]['dt_txt'].split(' ')[0],
    'day2_morning': {
    'Temperature': str(round(float(json_object['list'][13]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][13]['main']['pressure'],
    'Humidity':json_object['list'][13]['main']['humidity'],
    'Description':json_object['list'][13]['weather'][0]['description'],
    'Icon':json_object['list'][13]['weather'][0]['icon'],
    'Time': json_object['list'][13]['dt_txt'].split(' ')[1]
    },
    'day2_noon': {
    'Temperature': str(round(float(json_object['list'][15]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][15]['main']['pressure'],
    'Humidity':json_object['list'][15]['main']['humidity'],
    'Description':json_object['list'][15]['weather'][0]['description'],
    'Icon':json_object['list'][15]['weather'][0]['icon'],
    'Time': json_object['list'][15]['dt_txt'].split(' ')[1]
    },
    'day2_evening': {
    'Temperature': str(round(float(json_object['list'][17]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][17]['main']['pressure'],
    'Humidity':json_object['list'][17]['main']['humidity'],
    'Description':json_object['list'][17]['weather'][0]['description'],
    'Icon':json_object['list'][17]['weather'][0]['icon'],
    'Time': json_object['list'][17]['dt_txt'].split(' ')[1]
    },
    }
    """
    DAY 3
    """
    day3_pred={
    'Date':json_object['list'][21]['dt_txt'].split(' ')[0],
    'day3_morning': {
    'Temperature': str(round(float(json_object['list'][21]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][21]['main']['pressure'],
    'Humidity':json_object['list'][21]['main']['humidity'],
    'Description':json_object['list'][21]['weather'][0]['description'],
    'Icon':json_object['list'][21]['weather'][0]['icon'],
    'Time': json_object['list'][21]['dt_txt'].split(' ')[1]
    },
    'day3_noon': {
    'Temperature': str(round(float(json_object['list'][23]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][23]['main']['pressure'],
    'Humidity':json_object['list'][23]['main']['humidity'],
    'Description':json_object['list'][23]['weather'][0]['description'],
    'Icon':json_object['list'][23]['weather'][0]['icon'],
    'Time': json_object['list'][23]['dt_txt'].split(' ')[1]
    },
    'day3_evening': {
    'Temperature': str(round(float(json_object['list'][25]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][25]['main']['pressure'],
    'Humidity':json_object['list'][25]['main']['humidity'],
    'Description':json_object['list'][25]['weather'][0]['description'],
    'Icon':json_object['list'][25]['weather'][0]['icon'],
    'Time': json_object['list'][25]['dt_txt'].split(' ')[1]
    },
    }

    """
    DAY4
    Store day4 values from morning to evening
    """
    day4_pred={
    'Date':json_object['list'][29]['dt_txt'].split(' ')[0],
    'day4_morning': {
    'Temperature': str(round(float(json_object['list'][29]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][29]['main']['pressure'],
    'Humidity':json_object['list'][29]['main']['humidity'],
    'Description':json_object['list'][29]['weather'][0]['description'],
    'Icon':json_object['list'][29]['weather'][0]['icon'],
    'Time': json_object['list'][29]['dt_txt'].split(' ')[1]
    },
    'day4_noon': {
    'Temperature': str(round(float(json_object['list'][31]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][31]['main']['pressure'],
    'Humidity':json_object['list'][31]['main']['humidity'],
    'Description':json_object['list'][31]['weather'][0]['description'],
    'Icon':json_object['list'][31]['weather'][0]['icon'],
    'Time':json_object['list'][31]['dt_txt'].split(' ')[1]
    },
    'day4_evening': {
    'Temperature': str(round(float(json_object['list'][33]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][33]['main']['pressure'],
    'Humidity':json_object['list'][33]['main']['humidity'],
    'Description':json_object['list'][33]['weather'][0]['description'],
    'Icon':json_object['list'][33]['weather'][0]['icon'],
    'Time': json_object['list'][33]['dt_txt'].split(' ')[1]
    },
    }
    """
    DAY 5
    Store day5 values from morning to noon
    """
    day5_pred = {
    'Date':json_object['list'][37]['dt_txt'].split(' ')[0],
    "day5_morning": {
    'Temperature': str(round(float(json_object['list'][37]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][37]['main']['pressure'],
    'Humidity':json_object['list'][37]['main']['humidity'],
    'Description':json_object['list'][37]['weather'][0]['description'],
    'Icon':json_object['list'][37]['weather'][0]['icon'],
    'Time': json_object['list'][37]['dt_txt'].split(' ')[1]
    },
    'day5_noon': {
    'Temperature': str(round(float(json_object['list'][39]['main']['temp'])-273.15, 2)),
    'Pressure' : json_object['list'][39]['main']['pressure'],
    'Humidity':json_object['list'][39]['main']['humidity'],
    'Description':json_object['list'][39]['weather'][0]['description'],
    'Icon':json_object['list'][39]['weather'][0]['icon'],
    'Time': json_object['list'][39]['dt_txt'].split(' ')[1]
    },
    }
    return render_template('weather.html', data_descr=data_descr, day1_pred=day1_pred, day2_pred=day2_pred, day3_pred=day3_pred, day4_pred=day4_pred, day5_pred=day5_pred)

if __name__=='__main__':
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI']= database_file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(debug=True)
