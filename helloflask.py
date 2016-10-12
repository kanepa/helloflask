from flask import Flask, render_template

app = Flask(__name__)



albums =[{
    'artist': 'Madonna',
    'title' : 'True Blue',
    'year' : '1987'
}]

genres =['rock', 'blues', 'pop']

super = ['batman', 'superman', 'spiderman']

user = ['ironman', 'antman', 'robin']

ages = {
    'bob': '43',
    'alice': '29'

}


artists = [{

    'id': '1',
    'name': 'Gandolf',
    'title': 'The lord of the Rings'
    },
    {   'id':'2',
    'name': 'Patterson',
    'tile': 'walk alone'
     },
    {
    'id':'3',
    ''
    ''
    'name': 'Fletcher',
    'title': 'West Brom'
}]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/albums')
def list_albums():
    return render_template('helloflask.html', albums=albums, genres=genres, super=super)

@app.route('/albums')
def get_albums():
    return render_template("albums.html",albums=albums)

@app.route('/artists')
def get_artists():
    return render_template("artists.html", artists=artists, super=super)


@app.route('/artists/<id>')
def get_artist_details(id):
    return render_template("artist_details.html", artists=artists)

@app.route('/users/<user>')
def user(user):
    age = ages.get(user)
    return render_template('helloflask.html', user=user, age=age)


if __name__ == '__main__':
    app.run()
