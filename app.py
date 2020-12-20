from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #home page with get and post methods

def home():
    weight = ''
    height = ''
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = int(request.form.get('weight')) / 2.2046226218
        height = int(request.form.get('height')) * 0.0254
        bmi = round(weight / (height **2))


    return render_template("index.html",
                            weight=weight,
                            height=height,
                            bmi=bmi)




app.run()