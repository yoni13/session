from flask import Flask, request, redirect, url_for
import os
app = Flask(__name__)
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            return 'idk where is files'
        request.files['file'].save(os.path.join('C:\\Users\\yoni9\\Downloads\\session\\data'),request.files['file'].filename)
        return ''
if __name__ == '__main__':
    app.run(debug=True,port=80)