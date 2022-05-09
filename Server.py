# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import Flask, jsonify, request, abort, make_response, json
from lxml import etree
from collections import namedtuple
import os.path
import ReadJSON
import Dev.params as params
from Idoc import *
from Product import *
from ProductUnit import *
from ProductGTIN import *
from ProductDescription import *
from MaterialGroup import *
from Planogram import *
import OperatingDT as OperatingDT
import Queries as Queries
import preprocessXml as preprocessXml
import PostOperations as PostOperations
app = Flask(__name__)

class ProductGroup:
    pass

class ShelfInfo:
    pass

idocArray=[]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/uploadidoc', methods=['POST'])
def uploadidoc():
    print "request received"
    file_object = open('ShelfLayerDebug.txt', 'a')
    ReadJSON.init()
    products = preprocessXml.processXML(request.data)
    POSTDATA = True;
    productjson       =   PostOperations.Post(products,15)
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=3456)
