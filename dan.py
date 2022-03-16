from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
	return render_template('index.html') 


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def file_append(data):
	with open('database.txt', mode='a') as database:
		name = data['name']
		email = data['email']
		phone = data['phoneNumber']
		message = data['message']
		database.write(f'name:{name},\nemail:{email},\nphone:{phone},\nmessage:{message}\n \n')
	

@app.route('/message', methods=['POST', 'GET'])
def message():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	file_append(data)
    	return redirect('/thanks.html')
    else:
    	return 'someting went worng'

