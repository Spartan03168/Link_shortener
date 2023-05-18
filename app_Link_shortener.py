from datetime import datetime
from flask import Flask,render_template,request,redirect, url_for
from repo_students import Link,repository


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def basic_component():
    if request.method == "POST":
        url = request.form["Link"]
        hash_id = str(abs(hash(request.form["Link"])))[:7]
        link = Link(url=url,hash_id=hash_id,created_at=datetime.utcnow())
        repository.create(link)
        return redirect(url_for("links_storage_review"))

    return render_template("index.html")

@app.route("/data",methods=["GET","POST"])
def links_storage_review():
    links = repository.get()
    return render_template("links.html",links= links)

@app.route("/<hash_id>",methods=["GET","POST"])
def redirector(hash_id):
    hash_id_stored = repository.get(hash_id=hash_id)
    return redirect(hash_id_stored.url)


if __name__ == "__main__":
    app.run(debug = True)