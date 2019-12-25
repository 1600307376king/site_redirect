from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_pyfile('./config/setting.py')


@app.route('/pp/')
def hello_world():
    url = request.url
    print(url)
    return render_template('jump.html', url=url)


if __name__ == '__main__':
    app.run()
