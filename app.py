from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def registration_form():
    return render_template('reg.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)