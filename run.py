from flask import Flask,render_template,request, url_for, redirect
app = Flask(__name__)

posts = [1,2,"hola"]


@app.route("/")
def index():
    page = request.args.get("page",1)
    list = request.args.get("page",10)
    return render_template("index.html", num_post = len(posts))


@app.route("/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title = slug)


@app.route("/admin/post")
@app.route("/admin/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id = post_id)

@app.route("/signup/", methods=["GET","POST"])
def show_signup_form():
    if request.form == "POST":
       name =  request.form["name"]
       email = request.form["email"]
       password = request.form["pass"]
       
       next = request.args.get("next", None)
       
       if next:
           return redirect(next)
       return redirect(url_for("index"))
    return render_template("signup_form.html")