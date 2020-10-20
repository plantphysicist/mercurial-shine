from flask import Flask
import socketio

static_files = {
    '/': 'index.html',
    '/script.js': 'script.js',
    '/style.css': 'style.css'
}

sio = socketio.Server(async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app, static_files=static_files)

@sio.event
def connect(sid, environ):
    print('sending hey')
    sio.emit('hey', {'text': 'heyy!!', 'x': 25, 'y': 50})

@sio.on('hello')
def hello(sid, *data):
    print(f'hello {data[0]}')

@sio.on('command')
def command_handler(sid, *data):
    print(data)

if __name__ == '__main__':
    app.run(threaded=True)