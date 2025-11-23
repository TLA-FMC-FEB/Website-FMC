from flask import Flask, render_template
from fmc33index import get_fmc33index_data, get_fmc33index_info

app = Flask(__name__)

dates, values = get_fmc33index_data()
fmc33index_info = get_fmc33index_info()
largest_market_cap = fmc33index_info[0]
smallest_market_cap = fmc33index_info[1]
mean_market_cap = fmc33index_info[2]
median_market_cap = fmc33index_info[3]
largest_constituent = fmc33index_info[4]
smallest_constituent = fmc33index_info[5]
weight_largest_constituent = fmc33index_info[6]
weight_top10_constituent = fmc33index_info[7]

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

@app.route('/fmc33index')
def fmc33index():

    return render_template("fmc33index.html",
                           dates=dates,
                           values=values,
                           largest_market_cap = f"Rp {largest_market_cap:,.0f}",
                           smallest_market_cap = f"Rp {smallest_market_cap:,.0f}",
                           mean_market_cap = f"Rp {mean_market_cap:,.0f}",
                           median_market_cap = f"Rp {median_market_cap:,.0f}",
                           largest_constituent = largest_constituent,
                           smallest_constituent = smallest_constituent,
                           weight_largest_constituent = format(weight_largest_constituent, ".0%"),
                           weight_top10_constituent = format(weight_top10_constituent, ".0%")
                           )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)