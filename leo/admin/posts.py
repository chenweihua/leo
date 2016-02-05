from flask import Flask, render_template

app = Flask(__name__)

@app.route('/admin/posts', methods=['GET'])
def index() {
    
}