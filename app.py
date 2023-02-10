import pickle

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        
        nature = request.form['nature']
        fight = request.form['fight']
        cook = request.form['cook']
        clean = request.form['clean']
        
        model = pickle.load(open('model', 'rb'))
        
        li = []
        
        if nature == 'Good':
            li.append(1)
            li.append(0)        
        if nature == 'Average':
            li.append(0)
            li.append(0)    
        if nature == 'Worst':
            li.append(0)
            li.append(1)
            
        if fight == 'Fights':
            li.append(0)
        if fight == 'Not Fights':
            li.append(1)
            
        if cook == 'No':
            li.append(0)
        if cook == 'Yes':
            li.append(1)
            
        if clean == 'No':
            li.append(0)
        if clean == 'Yes':
            li.append(1)
        
        listt = [li]
        result = model.predict(listt)
        
        res = 'str'
        
        if result[0] == 0:
            res = 'The Prisoner has Worst Behaviour'
        elif result[0] == 1:
            res = 'The Prisoner has Average Behaviour'
        elif result[0] == 2:
            res = 'The Prisoner has Good Behaviour'
        else:
            res = "Unknown Error"
    
    return render_template('output.html', result=res)

if __name__ == "__main__":
    app.run()