from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/<name>', methods=['POST', 'GET'])
def index(name=None):
    if name == None:
        name = ''
	return render_template('index.html', name=name)

@app.route('/admin', methods=['POST', 'GET'])
def admin(name=None):
    resp = make_response(render_template('admin.html'))
    resp.headers['X-Powered-By'] = 'Leo'
    resp.set_cookie('SESSION_ID', 'DU998IU')
    return resp

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    return resp

if __name__ == "__main__":
	app.run()