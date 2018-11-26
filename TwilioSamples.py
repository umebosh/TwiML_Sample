from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
import  os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/call', methods=['POST'])
def twliml():
    f = open(os.path.split(__file__)[0] + "/twiml.xml")
    print(request.headers)
    print("body: %s" % request.get_data())

    return Response(response=f, content_type='application/xml')

if __name__ == '__main__':
    app.run()
