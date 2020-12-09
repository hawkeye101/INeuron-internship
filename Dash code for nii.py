#!/usr/bin/env python
# coding: utf-8

# In[88]:


import datetime

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

#!pip install chardet
import chardet

#!pip install nibabel
import nibabel as nib
import os

import base64
import datetime
import io
from PIL import Image

import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            html.Button('Upload File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
])

import base64, zlib

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    print(content_type)
    print(content_string[:20])
    decoded_data = zlib.decompress(base64.b64decode(content_string))

#    decoded = base64.b64decode(content_string)
#    image = nib.load(decoded).get_fdata()
    #    q = np.frombuffer(decoded, dtype=np.float64)

    #print(np.allclose(q, t))
    
    # print(size(decoded))
    # print(decoded)
    # chardet.detect(decoded)

    #file = open('test.txt', 'w') 
    #file.write(str(decoded,'utf-8')) 
    #file.close() 
    #io.StringIO(decoded.decode('utf-8'))
    #nib.save(decoded, os.path.join('build', 'input_image.nii.gz'))  

    return html.Div([
        #html.H5(filename),
        #html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        #html.Img(src=contents),
        #html.Hr(),

        #html.Div(decoded)
        #html.Div(type(decoded))

        #html.Div('Raw Content'),
        #html.Pre(contents[0:200] + '...', style={
        #    'whiteSpace': 'pre-wrap',
        #    'wordBreak': 'break-all'
        #})
    ])


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

""" 
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
#numpy array encoder to encode numpy 
#array for creating a json response.

#Args:
#JSONEncoder (ndarray): 3d image array
	def default(self, obj):
		if isinstance(obj, np.ndarray):
			return obj.tolist()
		return JSONEncoder.default(self, obj) 
 """

if __name__ == '__main__':
    app.run_server(port='8080', debug=True, use_reloader = False)

