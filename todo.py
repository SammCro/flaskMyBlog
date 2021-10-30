from flask import Flask,render_template,flash,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/İlkay Samet/Desktop/ToDoApp/todo.db"
db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    status = db.Column(db.Boolean)


@app.route("/")
def MainPage():

    todo = ToDo.query.all()


    return render_template("mainpage.html",todos = todo)

@app.route("/delete/<string:id>")
def Delete(id):
    todo = ToDo.query.filter_by(id = id).first()

    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("MainPage"))

@app.route("/complete/<string:id>")
def Update(id):
    todo = ToDo.query.filter_by(id=id).first()

    todo.status = not todo.status
    db.session.commit()

    return redirect(url_for("MainPage"))

@app.route("/add",methods=["POST"])
def Add():
    title = request.form.get("title")
    status = False

    todo = ToDo(title = title , status = status)  

    db.session.add(todo)
    db.session.commit()


    return redirect(url_for("MainPage"))







if __name__  == "__main__":
    db.create_all()
    app.run(debug=True)
