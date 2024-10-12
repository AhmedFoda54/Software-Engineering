from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        return f"Hello, {first_name} {last_name}! Form submitted successfully."

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)
