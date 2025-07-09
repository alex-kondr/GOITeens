from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello world!"


@app.get("/get-test/")
def get_test():
    return "Тестовий GET маршрут"


@app.post("/post-test/")
def post_test():
    return "Тестовий POST маршрут"


if __name__ == "__main__":
    app.run()
