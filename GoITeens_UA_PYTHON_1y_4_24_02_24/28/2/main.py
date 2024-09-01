from flask import Flask, render_template, request, abort


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.get("/")
def index():
    return {
            "name": "alex",
            "tel":
                {1: "05012345678",
                2: "1234654"
                }
        }


@app.get("/get-param/")
def get_param():
    print(request.args)
    return request.args


@app.get("/test-post/")
@app.post("/test-post/")
def test_post():
    print(request.form)
    return render_template("test_post.html", form=request.form.items())


@app.errorhandler(404)
def error_handler(error):
    print(request.base_url)
    url = request.base_url
    return render_template("error.html", url=url), 404


@app.get("/abort-test/")
def abort_test():
    password = request.args.get('password')
    if password == "1234":
        return "Ласкаво просимо"
    else:
        abort(401)



if __name__ == "__main__":
    app.run()