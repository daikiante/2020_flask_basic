# render_template => templatesからレンダリングを作成する
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# appがFlaskとして扱う(デコレーターと同じ名前)
app = Flask(__name__)

# Flaskに設定ファイルの指定をする
app.config.from_object('app.config')

db = SQLAlchemy(app)

# ルーティングを書いたファイルを読み込む
from app.views import index
