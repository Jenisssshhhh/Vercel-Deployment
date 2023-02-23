from flask import Flask,render_template,request,redirect
import pickle

app = Flask(__name__,template_folder='template')
  

'''@app.route('/')
def ios():
    return render_template('link.html')'''

@app.route('/',methods = ['POST','GET'])
def jen():
    if request.method == "POST":
        model = pickle.load(open('clustering.pkl','rb'))
        result = model.predict([[request.form['a'],request.form['s']]])
        print(result)
        return render_template('index.html',result = str(result))
    else:
       return render_template('index.html',result=False)



if __name__ =='__main__':
    app.run(debug=True)