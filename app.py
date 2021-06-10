from flask import Flask, render_template, request, jsonify  #서버 Flask

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')   #templates의 html 불러오는거임

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)

#크롬 키고 주소창에 localhost:5001쳐보셈!
##위 과정은 로컬 서버 생성과정... 지금 내 컴에서 돌아가는 서버를 내 컴의 브라우저로 접속해본거 #########
####로컬 개발 환경#######


# @app.route('/mypage')
# def mypage():
#     return 'This is mypage!'

#-------------아래는 url 분리 하는거 지금은 딱히 안씀! 페이지 넘어가거나 할 떄 쓰자--------

# @app.route('/test', methods=['GET'])    #GET는 읽어오기만 하는거
# def test_get():
#    title_receive = request.args.get('title_give')   #브라우저에서 ajax로 코딩한 부분에 title_give 값이 있으면 불러오는거
#    # ajax에서 'title_give' 못찾으면 None 출력
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET! 완료!'})
#
# @app.route('/test', methods=['POST'])   #POST는 읽고 수정도 가능한거
# def test_post():
#    title_receive = request.form['title_give']   #위 request.args.get('title_give')랑 역할은 같은데 코드만 다른... 그런것
#    #ajax에서 'title_give' 못찾으면 에러남!
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 POST! 완료!'})

####url 분리####