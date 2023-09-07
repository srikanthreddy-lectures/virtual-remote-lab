from flask import Flask
from flask import render_template
import subprocess
from subprocess import Popen, PIPE
from flask import jsonify
from flask import session
from flask import request
from flask import redirect
from flask import url_for
import os
import shutil
import re


app = Flask(__name__)

app.config['LAB_FOLDER'] = './static/users/'

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

regex = r"\[90m|\[32m|\[1m|\[0m|[\\]\w+"


ansi_escape = re.compile(regex, flags=re.IGNORECASE)


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}-->{session["id"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['id'] = "123"
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('id', None)
    return redirect(url_for('index'))

@app.route('/lab01/<name>')
def lab01(name):
    #return render_template('hello.html', name=name)
    #return {"username": name,}
    if name=='apply':
        cmd = ["sudo","bash","./lab01/lab01_apply.sh"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        out,err = p.communicate()
        mmessage=out.decode('utf-8')
        start_index = mmessage.find("ec_address")
        end_index = start_index + len(mmessage) 
        res=mmessage[start_index:start_index+27]
        return jsonify(message=res,success=True)

    elif name=='destroy':
        cmd = ["sudo","bash","./lab01/lab01_destroy.sh"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        out,err = p.communicate()
        mmessage=out.decode('utf-8')
        start_index = mmessage.find("ec_address")
        end_index = start_index + len(mmessage) 
        res=mmessage[start_index:start_index+27]
        return jsonify(message=res,success=True)
    #return 'You are not logged in'


@app.route('/mytest')
def mytest():
    return jsonify(message="https://google.com",success=True)

@app.route('/clone/<name>')
def clone(name):
    #return render_template('hello.html', name=name)
    #return {"username": name,}
    if name=='apply':
        cmd = ["sudo","bash","./clone/clone_apply.sh"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        out,err = p.communicate()
        mmessage=out.decode('utf-8')
        start_index = mmessage.find("ec_address")
        end_index = start_index + len(mmessage)
        res=mmessage[start_index:start_index+27]
        return jsonify(message=res,success=True)

    elif name=='destroy':
        cmd = ["sudo","bash","./lab01/lab01_destroy.sh"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        out,err = p.communicate()
        mmessage=out.decode('utf-8')
        start_index = mmessage.find("ec_address")
        end_index = start_index + len(mmessage)
        res=mmessage[start_index:start_index+27]
        return jsonify(message=res,success=True)
    #return 'You are not logged in'

@app.route('/labsession/<name>/<action>/<sessionid_>',methods=['GET', 'POST'])
def labsession(name, action, sessionid_):
    #return render_template('hello.html', name=name)
    #return {"username": name,}
    #print({session["id"]})
    if sessionid_ == session["id"]:
        user_folder = os.path.join(app.config['LAB_FOLDER'], session['username']+"/"+name+"/")
        os.makedirs(user_folder,exist_ok=True)
        #res= f"folder is created under the name {session['username']} and the full path is {user_folder}"
        # Providing the folder path
        origin = "./templates/lab01/"
        target = user_folder
        # Fetching the list of all the files
        files = os.listdir(origin)

        # Fetching all the files to directory
        for file_name in files:
            shutil.copy(origin+file_name, target+file_name)
        print("Files are copied successfully")
        if action == 'apply':

            cmd = ["sudo","bash",user_folder+"/lab01_apply.sh"]
            p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            out,err = p.communicate()
            mmessage=out.decode('utf-8')
            my=[]
            #for line in mmessage:
            print(mmessage)
            left,sep,right = mmessage.partition('Apply complete!')
            if sep: # True iff 'Output' in line
                res1=right[:500]
                aa1=ansi_escape.sub(' ', res1)
                ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', aa1 )
                my.append(ip)
                print(res1)
                for word in set(aa1.split(" ")):
                    #indexes = [w.start() for w in re.finditer(word, aa)]
                    match = re.search(r"\[(.+?)\]", word)
                    if match:
                        my.append(match.group(1))

                    
            print(my)
            return jsonify(message='http://'+my[0][0]+':8080/vnc.html',success=True)

        elif action=='destroy':
            cmd = ["sudo","bash",user_folder+"/lab01_destroy.sh"]
            p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            out,err = p.communicate()
            mmessage=out.decode('utf-8')
            my=[]
            #for line in mmessage:
            left,sep,right = mmessage.partition('ec_address')
            if sep: # True iff 'Output' in line
                res1=right[:1000]
                aa=ansi_escape.sub(' ', res1)
                for word in set(aa.split(" ")):
                    match = re.search(r"\[(.+?)\]", word)
                    if match:
                        my.append(match.group(1))

            #print(my)
            return jsonify(message=my,success=True)
        else:
            return jsonify(message="Invalid action",success=False)
    else:
        return jsonify(message="Invalid session",success=False)

