from flask import Flask, jsonify, request
from urllib.parse import quote
import requests

app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('config')
app.config.from_envvar('BOT_ID')
app.config.from_envvar('CHAT_ID')

@app.route('/', methods=['GET'])
def hello():
  return jsonify({
    "telegram_bot": "Hello There!"
  })

@app.route('/send', methods=['POST'])
def send_message():
  data = request.get_json()
  send_text = 'https://api.telegram.org/bot' + app.config['BOT_ID']
  send_text += '/sendMessage?chat_id=' + app.config['CHAT_ID']
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
