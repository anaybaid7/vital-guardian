from flask import Flask, render_template

app = Flask(__name__)

# Home route - renders the HTML page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on localhost
    app.run(debug=True)

