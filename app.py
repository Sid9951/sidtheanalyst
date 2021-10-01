from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/resume-pdf", methods=['GET'])
def download_file():
    path = "static/resume.pdf"

    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)