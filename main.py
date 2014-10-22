from flask import *

app = Flask(__name__)


def filter_string(string, filter_list):
    for filter in filter_list:
        string = string.replace(filter, "")
    return string

@app.route('/')
def index():
    return "The goal of each level will be to create an alert box. The server's filters will become progressively" + \
           " harder, requiring more complex payloads."


@app.route("/level1", methods=['GET', 'POST'])
def level1():
    if request.method == 'POST':
        print(request.form['xss'])
        return request.form['xss'] + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level2", methods=['GET', 'POST'])
def level2():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = xss.replace('alert', '')
        return xss + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level3", methods=['GET', 'POST'])
def level3():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert'])
        return xss + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level4", methods=['GET', 'POST'])
def level4():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img'])
        return xss + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level5", methods=['GET', 'POST'])
def level5():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img', 'onerror'])
        return xss + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level6", methods=['GET', 'POST'])
def level6():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img', 'onerror', 'javascript'])
        return xss + \
               "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level7", methods=['GET', 'POST'])
def level7():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img', 'onerror', 'javascript'])
        return "<pre>" + xss + \
               "</pre> <form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level8", methods=['GET', 'POST'])
def level8():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img', 'onerror', 'javascript'])
        return "<form method='POST'>XSS Me!<input type='text' name='xss' value='" +\
               xss + "'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.route("/level9", methods=['GET', 'POST'])
def level9():
    if request.method == 'POST':
        xss = request.form['xss']
        xss = filter_string(xss, ['script', 'alert', 'img', 'onerror', 'javascript', '<', '>'])
        return "<form method='POST'>XSS Me!<input type='text' name='xss' value='" +\
               xss + "'/><input type='submit'/></form>"
    return "<form method='POST'>XSS Me!<input type='text' name='xss'/><input type='submit'/></form>"


@app.after_request
def disable_xss_protection(req):
    req.headers.add('X-XSS-Protection', '0')
    return req

if __name__ == '__main__':
    app.run(debug=True)