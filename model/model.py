import pickle
from flask import Flask
from flask import request
import os

model_file_name="model.sav"
app = Flask(__name__)

class Model:
    def __init__(self):
        self.modelloaded=False
    def load_model(self,filename):
        if(self.modelloaded==False):
            self.model=pickle.load(open(filename, 'rb'))
    def predict(self,input):
        return self.model.predict(input)

@app.route("/classify",methods=['GET','POST'])
def classify():
    if(request.method =="POST"):
        pl = request.form.get("pl")
        pw = request.form.get("pw")
        sl = request.form.get("sl")
        sw = request.form.get("sw")
    else:
        pl = request.args.get("pl")
        pw = request.args.get("pw")
        sl = request.args.get("sl")
        sw = request.args.get("sw")

    result=model.predict([[pl,pw,sl,sw]])[0]
    return result

model=Model()
model.load_model(os.getcwd()+"\\"+model_file_name)

if __name__=="__main__": 
    app.run()



