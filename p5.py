from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
   msg ='<i>  Hello %s! </ i>' % name
   msg += '<p> enjoy the flask code! </p>'
   msg += '<p>  have a greate day! </p>'
   return msg
   if __name__ == '__main__':
    app.run()