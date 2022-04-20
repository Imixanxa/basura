from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, I want a Wordinpeace"
if __name__ == '__main__':
    app.run(port=5000, debug = True )


#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