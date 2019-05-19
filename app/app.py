import os
from datetime import datetime, date
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
    try:
        city=request.form['city_name']
        r=requests.get('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&mode=json&appid=e0fc2d0b038108cd17f1b71026ece2ce')
        json_object = r.json()
        """
        generating a list of indices for data to be presented to the user from the
        api response obtained
        """
        api_index=[]
        current_date=date.today()
        for num in range(len(json_object['list'])):
            dt_txt=json_object['list'][num]['dt_txt'].split(' ')[0]
            forecast_date=datetime.strptime(dt_txt, '%Y-%m-%d').date()
            if forecast_date>current_date:
                api_index.append(num)
        """
        getting the index values for obtaining weather values for morning, noon evening.
        """
        print(len(api_index))
        morning=[]
        noon=[]
        evening=[]
        for num in api_index:
            if json_object['list'][num]['dt_txt'].split(' ')[1]=='09:00:00':
                morning.append(num)
            if json_object['list'][num]['dt_txt'].split(' ')[1]=='12:00:00':
                noon.append(num)
            if json_object['list'][num]['dt_txt'].split(' ')[1]=='15:00:00':
                evening.append(num)

        print(api_index)
        print(morning)
        print(noon)
        print(evening)
        print(json_object['list'][evening[3]]['dt_txt'].split(' ')[0])
        """
        information of requested city
        """
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
        'Date':json_object['list'][morning[0]]['dt_txt'].split(' ')[0],
        'day1_morning':{
        'Temperature': str(round(float(json_object['list'][morning[0]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][morning[0]]['main']['pressure'],
        'Humidity':json_object['list'][morning[0]]['main']['humidity'],
        'Description':json_object['list'][morning[0]]['weather'][0]['description'],
        'Icon':json_object['list'][morning[0]]['weather'][0]['icon'],
        'Time': json_object['list'][morning[0]]['dt_txt'].split(' ')[1]
        },

        'day1_noon':{
        'Temperature': str(round(float(json_object['list'][noon[0]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][noon[0]]['main']['pressure'],
        'Humidity':json_object['list'][noon[0]]['main']['humidity'],
        'Description':json_object['list'][noon[0]]['weather'][0]['description'],
        'Icon':json_object['list'][noon[0]]['weather'][0]['icon'],
        'Time': json_object['list'][noon[0]]['dt_txt'].split(' ')[1]
        },
        'day1_evening': {
        'Temperature': str(round(float(json_object['list'][evening[0]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][evening[0]]['main']['pressure'],
        'Humidity':json_object['list'][evening[0]]['main']['humidity'],
        'Description':json_object['list'][evening[0]]['weather'][0]['description'],
        'Icon':json_object['list'][evening[0]]['weather'][0]['icon'],
        'Time': json_object['list'][evening[0]]['dt_txt'].split(' ')[1]
        },
        }
        """
        DAY 2
        """
        day2_pred={
        'Date':json_object['list'][morning[1]]['dt_txt'].split(' ')[0],
        'day2_morning': {
        'Temperature': str(round(float(json_object['list'][morning[1]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][morning[1]]['main']['pressure'],
        'Humidity':json_object['list'][morning[1]]['main']['humidity'],
        'Description':json_object['list'][morning[1]]['weather'][0]['description'],
        'Icon':json_object['list'][morning[1]]['weather'][0]['icon'],
        'Time': json_object['list'][morning[1]]['dt_txt'].split(' ')[1]
        },
        'day2_noon': {
        'Temperature': str(round(float(json_object['list'][noon[1]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][noon[1]]['main']['pressure'],
        'Humidity':json_object['list'][noon[1]]['main']['humidity'],
        'Description':json_object['list'][noon[1]]['weather'][0]['description'],
        'Icon':json_object['list'][noon[1]]['weather'][0]['icon'],
        'Time': json_object['list'][noon[1]]['dt_txt'].split(' ')[1]
        },
        'day2_evening': {
        'Temperature': str(round(float(json_object['list'][evening[1]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][evening[1]]['main']['pressure'],
        'Humidity':json_object['list'][evening[1]]['main']['humidity'],
        'Description':json_object['list'][evening[1]]['weather'][0]['description'],
        'Icon':json_object['list'][evening[1]]['weather'][0]['icon'],
        'Time': json_object['list'][evening[1]]['dt_txt'].split(' ')[1]
        },
        }
        """
        DAY 3
        """
        day3_pred={
        'Date':json_object['list'][morning[2]]['dt_txt'].split(' ')[0],
        'day3_morning': {
        'Temperature': str(round(float(json_object['list'][morning[2]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][morning[2]]['main']['pressure'],
        'Humidity':json_object['list'][morning[2]]['main']['humidity'],
        'Description':json_object['list'][morning[2]]['weather'][0]['description'],
        'Icon':json_object['list'][morning[2]]['weather'][0]['icon'],
        'Time': json_object['list'][morning[2]]['dt_txt'].split(' ')[1]
        },
        'day3_noon': {
        'Temperature': str(round(float(json_object['list'][noon[2]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][noon[2]]['main']['pressure'],
        'Humidity':json_object['list'][noon[2]]['main']['humidity'],
        'Description':json_object['list'][noon[2]]['weather'][0]['description'],
        'Icon':json_object['list'][noon[2]]['weather'][0]['icon'],
        'Time': json_object['list'][noon[2]]['dt_txt'].split(' ')[1]
        },
        'day3_evening': {
        'Temperature': str(round(float(json_object['list'][evening[2]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][evening[2]]['main']['pressure'],
        'Humidity':json_object['list'][evening[2]]['main']['humidity'],
        'Description':json_object['list'][evening[2]]['weather'][0]['description'],
        'Icon':json_object['list'][evening[2]]['weather'][0]['icon'],
        'Time': json_object['list'][evening[2]]['dt_txt'].split(' ')[1]
        },
        }

        """
        DAY4
        Store day4 values from morning to evening
        """
        day4_pred={
        'Date':json_object['list'][morning[3]]['dt_txt'].split(' ')[0],
        'day4_morning': {
        'Temperature': str(round(float(json_object['list'][morning[3]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][morning[3]]['main']['pressure'],
        'Humidity':json_object['list'][morning[3]]['main']['humidity'],
        'Description':json_object['list'][morning[3]]['weather'][0]['description'],
        'Icon':json_object['list'][morning[3]]['weather'][0]['icon'],
        'Time': json_object['list'][morning[3]]['dt_txt'].split(' ')[1]
        },
        'day4_noon': {
        'Temperature': str(round(float(json_object['list'][noon[3]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][noon[3]]['main']['pressure'],
        'Humidity':json_object['list'][noon[3]]['main']['humidity'],
        'Description':json_object['list'][noon[3]]['weather'][0]['description'],
        'Icon':json_object['list'][noon[3]]['weather'][0]['icon'],
        'Time':json_object['list'][noon[3]]['dt_txt'].split(' ')[1]
        },
        'day4_evening': {
        'Temperature': str(round(float(json_object['list'][evening[3]]['main']['temp'])-273.15, 2)),
        'Pressure' : json_object['list'][evening[3]]['main']['pressure'],
        'Humidity':json_object['list'][evening[3]]['main']['humidity'],
        'Description':json_object['list'][evening[3]]['weather'][0]['description'],
        'Icon':json_object['list'][evening[3]]['weather'][0]['icon'],
        'Time': json_object['list'][evening[3]]['dt_txt'].split(' ')[1]
        },
        }
        return render_template('weather.html', data_descr=data_descr, day1_pred=day1_pred, day2_pred=day2_pred, day3_pred=day3_pred, day4_pred=day4_pred)
    except:
        return redirect(url_for('index'))


if __name__=='__main__':
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI']= database_file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(debug=True)
