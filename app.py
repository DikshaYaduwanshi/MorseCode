from flask import Flask, render_template, Response,request,url_for
import os
from werkzeug.utils import redirect, secure_filename
#from test import Camera
#from test import Detectmorse
#import testflask
import time
from f import *


app = Flask(__name__)
#morse = Detectmorse()

@app.route('/',methods=['GET'])
@app.route('/index.html')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/contact.html')
def something():
    return render_template('contact.html')

@app.route('/about.html')
def something1():
    return render_template('about.html')

@app.route('/eye.html')
def eye():
    return render_template('eye.html')

@app.route('/eye1.html')
def eye1():
    return render_template('eye1.html')

@app.route('/morse.html')
def morse():
    return render_template('morse.html')

@app.route('/morse1.html')
def morse1():
    return render_template('morse1.html')

@app.route('/morse2.html')
def morse2():
    return render_template('morse2.html')

#UPLOAD_FOLDER="D:/Palak/minor/EyeMorseCode"
#ALLOWED_EXTENSIONS={'mp4','mov','mkv','avi','wmv'}
#app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

#def allowedFile(filename):
    #return '.' in filename and \
           #filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader',methods=['GET'])
def upload_file():
    file=request.args.get('file')
    mytest(file)
    return file
  
  
  
  
  
  
  
   #if request.method == 'POST':
    #  f = request.files['file']
    #  mytest(f)
   #   if f and allowedFile(f.filename):
     # f.save(secure_filename(f.filename))
     
      #return 'file uploaded successfully'
   #return None
  
   


#@app.route('/uploader?file=<f>')
#def execute():
 #   f=request.form['file']
  #  test1(f)
   # return render_template('morse.html')

@app.route('/me.html')
def execute():
    return render_template('me.html')

if __name__ == '__main__':
    app.run(debug=True)
