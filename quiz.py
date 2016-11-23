from flask import (
  Flask,
  render_template,
  send_file,
  request
)

import os
import random
import urllib2
import re
import uuid

from image import Image

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('main.html')

@app.route("/upload")
def upload():
  url = request.args['url']
  name = str(uuid.uuid4().int)

  m = re.search(r'[.]([^/]+)$', url)
  if m:
    name += m.group()

  image_file = urllib2.urlopen(url)
  with open('images/' + name, 'wb') as output:
    output.write(image_file.read())
  
  print name

  return name

@app.route("/random_image")
def random_image():
  image = random.choice(images())
  return send_file('images/' + image.filename, mimetype=image.mimetype)

def images():
  return [Image.create_from_file(f) for f in os.listdir('images')]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
