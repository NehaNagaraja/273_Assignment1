from flask import Flask, render_template, request,redirect, url_for
from flaskext.uploads import (UploadSet, configure_uploads, IMAGES,UploadNotAllowed,SCRIPTS)


app = Flask(__name__)
#configure_uploads(app, programs)
programs = UploadSet('programs', SCRIPTS)

app.config['UPLOADED_PROGRAMS_DEST'] = '/home/neha/todo-api/flask/tmp/api/v1'
configure_uploads(app, (programs,))

@app.route('/api/v1/scripts', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'data' in request.files:
        filename = programs.save(request.files['data'])
        return filename
    else:
	return '/foo.py'

if __name__ == '__main__':
	app.run(host='localhost', port=8000, debug=True)
