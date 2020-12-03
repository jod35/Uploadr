from flask import(
            Flask,
            render_template,
            request,
            redirect,
            url_for,
            current_app,
            abort,
            send_from_directory
            )


from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=1024*1024
app.config['UPLOAD_EXTENSIONS']=['.gif','.png','.jpg']
app.config['UPLOAD_PATH']='uploads'


@app.route('/')
def index():
    files=os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html',files=files)


@app.route('/upload',methods=['POST'])
def upload_file():
    uploaded_file=request.files['file']

    filename=secure_filename(uploaded_file.filename)

    if filename !='':
        file_ext=os.path.splitext(filename)[1]

        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            abort(400)

    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],filename))

    return redirect(url_for('index'))




@app.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'],filename)


@app.errorhandler(400)
def file_too_large(error):
    return "The file is not of allowed type <a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)