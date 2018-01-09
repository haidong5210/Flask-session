from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'
	
	
if __name__ == '__main__':
	app.run()   
	"""
	内部是基于werkzeug做的socket请求
	run_simple(host, port, self, **options) 
	执行self
	请求进来会执行app的__call__方法
	"""
	
	