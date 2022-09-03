from flask import Flask, request, redirect, url_for
import os
app = Flask(__name__)
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        file = request.files['file']
        file.save(os.path.join('C:\\Users\\yoni9\\Downloads\\session\\data'), file.filename)
        return ''
if __name__ == '__main__':
    app.run(debug=True)