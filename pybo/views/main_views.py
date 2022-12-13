from flask import Blueprint,url_for # render_template 제거
from werkzeug.utils import redirect

#from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')
""" bp : 객체명
    __name__ : 모듈명인 "main_views"가 인수로 전달됨
    "main"은 : 블루프린트의 "별칭".  나중에 자주 사용할 url_for 함수에서 사용
    url_prefix : 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미
"""

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo_ Blue print!'

@bp.route('/')
def index():
    #question_list = Question.query.order_by(Question.create_date.desc())
    #return render_template('question/question_list.html', question_list=question_list)
    return redirect(url_for('question._list'))

"""
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
"""
