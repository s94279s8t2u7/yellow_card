from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import SocketIO,emit
import json


# token
# 讀入卡片
with open("card.json","r",encoding="utf-8") as f:
	data = json.load(f)
print(data[1])

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('story.html')

# 登入
@socketio.on('register')
def register(account_data):
	with open("test.txt",'w') as f:
		content="try it "
		f.write(content)
	print(account_data)
	socketio.emit('usernames',account_data)

@socketio.on('new_user_login')
def new_user_login():
	print('有人登入')
# 題目
@socketio.on('get_title')
def get_title():
	print('發題目')
# 發牌
@socketio.on('get_card')
def get_card():
	socketio.emit('give_user_card',data)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
