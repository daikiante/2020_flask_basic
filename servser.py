# app.pyで変数宣言したappを呼び出している
from app import app

# このファイルが呼ばれたら実行する
if __name__ == '__main__':
    app.run()