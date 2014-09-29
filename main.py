from flask import *

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True

@app.route('/', methods=['GET'])
def home():
  return app.send_static_file('index.html')



if __name__ == '__main__':
  app.run()
