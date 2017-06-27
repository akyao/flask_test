# -*- coding: utf-8 -*
# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        u"こんにちは、あなたの名前を入力してください",
        u"やあ！お名前は何ですか？",
        u"あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "welocome"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "hello"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
