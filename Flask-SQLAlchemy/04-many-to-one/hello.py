import os

from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 초기화
app = Flask(__name__)

# 초기화 - SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# 모델 정의
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    # Category 모델 참조
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    # many-to-one 참조 관계
    # one-to-many: backref는 dynamic lazy loading
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))
    
    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
        
        
# 뷰 함수와 라우팅
@app.route('/')
def index():
    p = Post.query.first()
    print(p.category)
    
    c = Category.query.first()
    print(c.posts.all())

    return '<h1>Many-to-One (bidrectional)</h1>'

# 서버 실행
if __name__ == '__main__':
    app.host = '127.0.0.1'
    app.port = 5000
    app.debug = True
    
    app.run()
