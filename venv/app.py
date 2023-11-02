from flask import Flask
app = Flask("My app")
 
@app.route('/')
def hello_name():
   return 'Hello World'
 
app.run(debug=True)
