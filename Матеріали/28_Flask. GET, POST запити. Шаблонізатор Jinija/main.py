from flask import Flask, render_template


app = Flask(__name__)


@app.get('/')
def index():
  return render_template ('base.html', title='jinja_test')


max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]


@app.get('/results')
def results():
  context={
     "title": "Results",
     "students": students,
     "test_name": test_name,
     "max_score": max_score,
  }
  return render_template("results.html", **context)


if __name__ == '__main__':
  app.run(debug=True)