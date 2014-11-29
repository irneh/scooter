import flask as f
import requests
import simplejson as json
import urlparse

from guides import guides

API = "https://scoot.io/api/object/"
app = f.Flask(__name__)
app.debug = True

@app.route("/")
def index():
  return "home"

@app.route("/go/<id>")
def go(id):
  r = requests.get(API + id)
  data = json.loads(r.text)
  return f.render_template('go.html', data=data)

@app.route("/guide/<id>")
def guide(id):
  data = []
  for i in guides[id]:
    r = requests.get(API + str(i))
    hike = json.loads(r.text)
    data.append(hike)
  return f.render_template('guide.html', data=data)

if __name__ == "__main__":
    app.run()
