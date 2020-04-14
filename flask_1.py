from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello,world'

@app.route('/list/')
def my_list():
    return 'my list'

@app.route('/p/<path:test>/')
def test_p(test):
    return 'test p, %s ' % test

@app.route('/article/<int:article_id>/')
def article_detail(article_id):
    return '您请求的文章是： %s' % article_id

@app.route('/search/<string:search_id>/')
def search_detail(search_id):
    return '您查找的内容是： %s' % search_id

@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心： %s' % user_id
import uuid
print(uuid.uuid4())

@app.route('/<any(blog, user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情： %s' % id
    else:
        return '用户详情： %s' % id

# 通过？形式传递参数
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    return '您通过查询字符串的方式传递的参数是: %s' % wd


if __name__ == "__main__":
    app.run(debug=True)



