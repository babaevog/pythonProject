from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('geniusproject.html')


@app.route("/index")
def index2():
    return render_template('index.html')


@app.route("/genius2")
def index3():
    return render_template('project2.html')


@app.route("/genius3")
def index4():
    return render_template('project4.html')


@app.route("/genius4")
def index5():
    return render_template('project6.html')


@app.route("/genius5")
def index6():
    return render_template('project8.html')



@app.route("/genius6")
def index7():
    return render_template('project10.html')


@app.route("/genius7")
def index8():
    return render_template('project12.html')


@app.route("/landing")
def index9():
    return render_template('index1.html')


@app.route("/contacts")
def index11():
    return render_template('project14.html')


@app.route("/skills")
def index12():
    return render_template('project15.html')


@app.route("/main")
def main():
    return "Ты куда полез"


@app.route("/user/<int:id>")
def user(id):
    return "Вы пользователь " + str(id)


if __name__ == "__main__":
    app.run(debug=False)