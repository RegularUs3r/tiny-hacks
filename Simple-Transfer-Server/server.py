from contextlib import redirect_stderr
from flask import Flask, flash, render_template, request, redirect, url_for, json
from werkzeug.utils import secure_filename
import pathlib
import os
import argparse

upload_folder = pathlib.Path().resolve()
allowed_extensios = {"zip"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = upload_folder
app.secret_key = 'super secret key'


@app.route('/')
def start():
    if request.path == "/":
        flash('This is a flash message')
        return redirect("/upload-file")

@app.route("/upload-file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename_slices = file.filename.split(".")
        if "."+filename_slices[-1] == ".zip":
            file = request.files["file"]
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return '''
                    <body>
                    <script>
                    window.location.href = "/"
                    </script>
                    </body>
                   '''
        else:
            return render_template("forbidden.html")
    return render_template("fileupload.html")



if __name__ == '__main__':
    parser =argparse.ArgumentParser()
    parser.add_argument("-p", "--port", metavar="", required=True)
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)