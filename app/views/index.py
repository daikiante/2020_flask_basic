# url_for : 名前解決が使えるようになる(html内で関数名を指定する)
from flask import render_template, url_for, request, redirect, session
from app import app
from app import db
from app.models.entries import Entry

# ルーティング
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/second')
def second():
    entry = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('second.html', entry=entry)

@app.route('/input', methods=['POST'])
def input():
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    
    # dbのセッションに上げてからコミット(保存)の処理
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('index'))