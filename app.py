from flask import Flask, render_template, request, redirect, url_for
import os
import string 
import random 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def secure_filename(filename, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(len(filename)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) + '.' + file.filename.rsplit('.', 1)[1].lower()
        if os.path.exists('/static/uploads') == False:
            os.mkdir('/static/uploads')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
