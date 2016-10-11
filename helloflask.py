from flask import Flask, render_template

app = Flask(__name__)



albums =[{
    'artist': 'Madonna',
    'title' : 'True Blue',
    'year' : '1987'
}]

genres =['rock', 'blues', 'pop']

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/albums')
def list_albums():
    return render_template('helloflask.html', albums=albums, genres=genres)

if __name__ == '__main__':
    app.run()
