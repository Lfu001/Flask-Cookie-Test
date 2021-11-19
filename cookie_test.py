from datetime import datetime
from flask import *
import uuid

app = Flask(__name__)


@app.route("/")
def root():
    cookie = request.cookies.get("user_id", None)
    if cookie is None:
        user_id = str(uuid.uuid4())
        has_cookie = False
    else:
        user_id = cookie
        has_cookie = True

    response = make_response(render_template("index.html", user_id=user_id, has_cookie=has_cookie))

    # Cookieの設定を行う
    max_age = 5  # 有効期間5秒
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('user_id', value=user_id, max_age=max_age, expires=expires, path='/', secure=None, httponly=False)

    # レスポンスを返す
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5555, host="0.0.0.0")
