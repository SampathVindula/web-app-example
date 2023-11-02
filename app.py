from flask import Flask

app = Flask("My app")
 
@app.route('/')
def hello_world():
    return 'Hello World'
 
app.run()
