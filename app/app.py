from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def call():
    username = request.form['username']
    return render_template('call.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
