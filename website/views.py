from flask import Blueprint, render_template, request, flash
import os
from dotenv import load_dotenv
import mysql.connector
import requests

load_dotenv()

views = Blueprint('views',__name__)

@views.route('/pump')
def pump():

    db = mysql.connector.connect(
        host= os.getenv('host'),
        user=os.getenv('user'),
        passwd=os.getenv('passwd'),
        database=os.getenv('database'),
        )



    '''Prepare data for line graph'''
    data = {
        "x" : [1,2,3],
        "y" : [3,2,1]
        }


    
    return render_template('pump.html', data = data)

@views.route('/water')
def water():

    db = mysql.connector.connect(
        host= os.getenv('host'),
        user=os.getenv('user'),
        passwd=os.getenv('passwd'),
        database=os.getenv('database'),
        )

    def select_value_db(select_what,select_from,select_howmany):
    
        mycursor = db.cursor()

        mycursor.execute(f"SELECT {select_what} FROM {select_from} ORDER BY id DESC LIMIT {select_howmany}")

        resoult = mycursor.fetchall()

        test_list = []
        value_list = []

        for i in resoult:
            test_list.append(i)
            

        for i in range(0,len(test_list)):
            value= list(f"{test_list[i]}")

            del value[0:1]
            del value[-2:]
            
            joined = "".join(value)

            value_list.append(joined)


        return value_list


    


    def preparing_points():
        points = []
        value_int = []
        value_list = select_value_db("value","water_use",288)

        for i in value_list:
            x = float(i)
            value_int.append(x)

        for i in range(1,288):
            b = value_int[-i]
            i = -i-1
            c = value_int[i]

            x = c-b
            points.append(x)


        return points

    def prepare_date():
        data_test_list = []
        date_list = []
        hour_list = []

        
        
        
        mycursor = db.cursor()


        

        mycursor.execute("SELECT date FROM heat_pump ")

        resoult = mycursor.fetchall()


        for x in resoult:
            data_test_list.append(x)

        for i in range(1,288):
            value = list(f"{data_test_list[-i]}")
            
            del value[0:2]
            del value[-3:]
            del value[10:]
            joined = "".join(value)
            date_list.append(joined)

        for i in range(1,288):
            value = list(f"{data_test_list[-i]}")
            
            del value[0:13]
            del value[-10:]
            
            joined = "".join(value)
            hour_list.append(joined)
        
        return hour_list
        

    '''Prepare data for line graph'''
    data = {
        "x" : prepare_date(),
        "y" : preparing_points()
        }


    return render_template('water.html', data = data )


@views.route('/solar')
def solar():

    solaredge = 'https://monitoringapi.solaredge.com/%20site/'+ os.getenv('site_id') + '/overview.json?api_key=' + os.getenv('api_key')
    json_data = requests.get(solaredge).json()


    class solaredge():
        @staticmethod
        def solardata():
            lastupdatetime = json_data['overview']['lastUpdateTime']
            totalenergythisyear = json_data['overview']['lifeTimeData']['energy']/1000
            lastyearenergy = json_data['overview']['lastYearData']['energy']/1000
            lastmonthenergy = json_data['overview']['lastMonthData']['energy']/1000
            lastdayenergy = json_data['overview']['lastDayData']['energy']/1000
            currentpower = json_data['overview']['currentPower']['power']
            return {'lastupdatetime':lastupdatetime,'totalenergythisyear': totalenergythisyear,'lastyearenergy': lastyearenergy,'lastmonthenergy': lastmonthenergy,'lastdayenergy': lastdayenergy,'currentpower':currentpower}
        
        
    return render_template('solar.html', data = solaredge.solardata())