#Simple file manager using the python and flask

from flask import Flask
from flask import render_template
from flask import redirect
import os
import subprocess
from flask import request

from sys import platform


#Create a web instance
app = Flask(__name__, template_folder='templatesFolder', static_folder='staticFile')

#handle the root
@app.route('/')
def root():
    if platform == 'win32':
        print("The program is running in the windows machine")
        return render_template('Index.html', currentWorkingDirectory = os.getcwd(), fileList = subprocess.check_output('dir /b', shell=True).decode('utf-8').split('\n'))
    elif platform == 'linux':
        print("The program is running in the linux machine")
    elif platform == 'mac':
        print("The program is running in the mac machine")


#For windows it is dir and for linux it is ls

#handle level ip command
@app.route('/parentDirectory')
def parentDirectory():
    #run level up command
    os.chdir('..')
    return redirect('/')

@app.route('/cd')
def cd():
    os.chdir(request.base_url)
    return redirect('/')


#Run the http server
if __name__ == '__main__':
    app.run(debug = True, threaded = True)
