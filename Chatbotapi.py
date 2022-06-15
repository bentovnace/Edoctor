from flask import Flask, request
from chat import start_chat
import requests
import json
app = Flask(__name__)

@app.route('/edoctor', methods=['GET','POST'])


def chatbot():
    chatInput = request.args.get('input')
    r = requests.get('http://coronavirus-19-api.herokuapp.com/countries/Vietnam')
    data =r.json()
    covid = f'Ca nhiễm:{data["cases"]}\nChết: {data["deaths"]} \nKhỏi:{data["recovered"]} \nSố ca nhiễm trong ngày: {data["todayCases"]}'
    if chatInput == "Diễn biến covid 19" or chatInput =="Tình hình covid 19" or chatInput == "Diễn biến covid 19 ở Việt Nam" or chatInput =="Tình hình covid 19 ở Việt Nam" or chatInput == "Số ca nhiễm" or chatInput =="Chết" :
        return covid
    else:
        return str(start_chat(chatInput))

if __name__  == "__main__":
    app.run(host ='0.0.0.0',port = '6868')
    