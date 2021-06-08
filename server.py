from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import SocketIO,emit
import json
# jwt驗證
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# 設定 JWT 密鑰
app.config['JWT_SECRET_KEY'] = 'this-should-be-change'
jwt.init_app(app)

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


@socketio.on('new_user_login')
def new_user_login():
	print('有人登入')
# 發牌
@socketio.on('get_card')
def get_card():
	print(data)
	socketio.emit('give_user_card',data)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
