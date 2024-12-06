from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template("about-us.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/bbri-lakukan-buyback')
def bbri_lakukan_buyback():
    return render_template("bbri-lakukan-buyback.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/research')
def research():
    return render_template("research.html")

@app.route('/latest')
def latest():
    return render_template("latest.html")

@app.route('/stock-watchlist')
def stock_watchlist():
    return render_template("stock-watchlist.html")

@app.route('/research-and-education')
def research_and_education():
    return render_template("research-and-education.html")

@app.route('/sharia')
def sharia():
    return render_template("sharia.html")

@app.route('/data-vision')
def data_vision():
    return render_template("data-vision.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


