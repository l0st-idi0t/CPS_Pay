from flask import Flask, jsonify, render_template, Response
from threading import Thread
from flask_restful import Resource, Api
import xlrd
import requests

app = Flask(__name__)
api = Api(app)


def run():
  app.run(host='0.0.0.0', port=8888)


class Empty(Resource):
    
        def __init__(self):
            pass
    
        def get(self):
            return {
                "Hello": "World"
            }


class Info(Resource):

    def __init__(self):
        self.fileName = self.request_salaries()

    def get(self, school, lastName, job, fte):
        return {
            "Hello": "World"
        }

    def request_salaries(self):
        url = "https://www.cps.edu/about/finance/employee-position-files/"
        response = str(requests.get(url).content)

        #find most recent salary file
        filePos = response.find("globalassets/cps-pages/about-cps/finance/employee-position-files/")
        fileURL = "https://www.cps.edu/" + response[filePos : filePos + 100]
        fileName = response[filePos + 65 : filePos + 100]

        #download file
        r = requests.get(fileURL)
        with open(fileName, 'wb') as f:
            f.write(r.content)

        return fileName


#api endpoint
api.add_resource(Empty, '/')
api.add_resource(Info, '/<string:school>/<string:lastName>/<string:job>/<float:fte>')


if __name__ == '__main__':
    t = Thread(target=run)
    t.start()