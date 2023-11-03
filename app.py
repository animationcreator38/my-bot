from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

return 'KISHAN484'

if __name__ == "___main___":
    app.run()
