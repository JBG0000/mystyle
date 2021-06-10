from flask import Flask, render_template, request, jsonify  #서버 만들때는 Flask 패키지 이용!

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('indexa.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)