from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
	return 'welcome to docker'

# main driver function
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
