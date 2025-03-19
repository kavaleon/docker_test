from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():

    return ('''
    <h1> Hello 1 </h1>
    <a href="/2/"> Second page </a> 
    ''')

@app.route('/2/')
def index2():
    return ('''
        <h1> Hello 2 </h1>
        <a href="/"> Main page </a> 
        ''')

app.run(debug=True, host='0.0.0.0')