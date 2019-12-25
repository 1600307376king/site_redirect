from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_pyfile('./config/setting.py')

# http://fw.newlifehealth.cn:8099/pp/?enc=58918e22003003000003
@app.route('/pp/')
def hello_world():
    enc_value = request.args.get('enc', '')

    filter_obj = 'http://fw.newlifehealth.cn:8099/pp/?enc=' + str(enc_value)
    return render_template('jump.html', url=filter_obj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
