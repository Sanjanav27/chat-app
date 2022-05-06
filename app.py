from logging import debug
from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
from gtts import gTTS
import os
# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

language ='en'

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( "/", methods = ["GET","POST"] )
def hello():
  return render_template( 'index.html' )
@app.route("/chatapp", methods = ["GET","POST"])
def chatapp():
  username=request.form["user-name"]
  return render_template('chatAppPage.html',username=username)

@app.route("/voice",methods=["GET","POST"])
def voice():
  message=request.form.get("message")
  print(message)
  # if request.method=='POST':
  #   if request.form['submit_button'] == 'Do Something':
  #     pass # do something
  return "sdc"

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )
