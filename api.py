from flask import Flask

app = Flask(__name__)

@app.route('/userscript.user.js')
def userscript():
    str = ""
    try:
        with open("highlighter.user.js", "r") as f:
            str = f.read()
    except Exception as e:
        print("Warning: Cannot read file.: ", e)

    return str

@app.route('/api/<string:vendor>')
def api(vendor):
    if vendor == "건율상사":
        return "YEP"
    else:
        return "NOP"
    
if __name__ == "__main__":
    app.run(port=8081)
