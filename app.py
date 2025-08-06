from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)


number_list = []

@app.route('/')
def welcome():
   
    return redirect(url_for('home'))

@app.route('/home')
def home():
    
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    global number_list

    if request.method == "POST":
        try:
            
            num = int(request.form.get("number"))
            number_list.append(num)
        except (TypeError, ValueError):
            pass  

       
        return redirect(url_for('home'))

   
    return jsonify({"value": number_list})

if __name__ == "__main__":
    app.run(debug=True)
