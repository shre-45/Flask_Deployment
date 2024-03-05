from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']
       
        try:
            matches = re.findall(regex_pattern, test_string)
            return render_template('results.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)
        except re.error:
            matches = ['Invalid regex pattern.']
            return render_template('results.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)
    return render_template('index.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
  
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        message = "The email ID is valid."
    else:
        message = "The email ID is invalid."
    return render_template('email_validation_result.html', message=message)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

