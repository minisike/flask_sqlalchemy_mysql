from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ctx = app.app_context()  #手动创建栈顶的应用上下文
ctx.push()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ww860512ww@127.0.0.1:3306/web"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)  # 先配置数据库app.config再创建db





class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(16))
    brief = db.Column(db.String(128))


if __name__ == '__main__':
    author = Author()
    author.id = input("请输入ID")
    author.name = input("请输入NAME")
    author.brief = input("请输入BRIEF")
    db.session.add(author)
    db.session.commit()
    ctx.push()