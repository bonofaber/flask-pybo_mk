import os

BASE_DIR = os.path.dirname(__file__)

#SQLite 데이터베이스 사용, 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False  #  SQLAlchemy의 이벤트 처리 옵션. False로 비활성화
SECRET_KEY = "dev"
