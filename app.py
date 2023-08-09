from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from waitress import serve
from form import UploadFileForm
from werkzeug.utils import secure_filename
import os
from jinja2 import BaseLoader, Markup, TemplateNotFound, nodes
import io

app=Flask(__name__)
app.config['SECRET_KEY']="secretkey"
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route("/", methods=["GET", "POST"])
def index():
    form=UploadFileForm()
    if form.validate_on_submit():
        file=form.file.data 
        file.save(os.path.join
                  (os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File Uploaded Successfully."
    return render_template("index.html", form=form)


@app.route("/download")
def download():
    return send_file("static/uploads/contract.docx", as_attachment=True)


if __name__=="__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080, threaded=True)
    #serve(app, host='0.0.0.0', port=8080, url_scheme="https")