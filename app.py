from flask import Flask,render_template,request,redirect,url_for,current_app,abort
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=1024*1024
app.config['UPLOAD_EXTENSIONS']=['.gif','.png','.jpg']
app.config['UPLOAD_PATH']='uploads'




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def upload_file():
    uploaded_file=request.files['file']

    filename=uploaded_file.filename

    if filename !='':
        file_ext=os.path.splitext(filename)[1]

        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            abort(400)

    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],filename))

    return redirect(url_for('index'))





if __name__ == "__main__":
    app.run(debug=True)