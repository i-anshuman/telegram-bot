from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from urllib.parse import quote
import requests
from os import environ

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config.from_object('config')

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
  return jsonify({
    "telegram_bot": "Hello There!"
  })

@app.route('/send', methods=['POST'])
@cross_origin()
def send_message():
  data = request.get_json()
  send_text = 'https://api.telegram.org/bot' + environ.get('BOT_ID')
  send_text += '/sendMessage?chat_id=' + environ.get('CHAT_ID')
  send_text += '&parse_mode=HTML&text=' + quote((
    "<b>New Message From Portfolio</b>\n\n"
    "<b>"
    "Name: <i>{name}</i>\n"
    "Email: <i>{email}</i>\n"
    "Message: <i>{message}</i>"
    "</b>"
  ).format(name=data.get('name'), email=data.get('email'), message=data.get('message')))

  res = requests.get(send_text)
  return res.json()
