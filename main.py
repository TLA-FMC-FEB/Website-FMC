import granian
from quart import Quart, render_template
from quart_rate_limiter import RateLimiter, RateLimit
from datetime import timedelta

app = Quart(__name__)

# Define multiple default limits
default_limits = [
    RateLimit(10, timedelta(seconds = 1)),    # 10 request per 1 second - changed from 5
    RateLimit(150, timedelta(minutes = 1)),  # 150 requests per minute - changed from 120
    RateLimit(1000, timedelta(hours = 1))    # 1000 requests per hour - no change
]

rate_limiter = RateLimiter(app, default_limits = default_limits)


@app.route('/')
async def index():
    return await render_template("index.html")
    
@app.route('/about')
async def about():
    return await render_template("about-us.html")
    
@app.route('/events')
async def events():
    return await render_template("events.html")

@app.route('/learn')
async def learn():
    return await render_template("learn.html")

@app.route('/coolify')
async def coolify():
    return await """
    <h1>Tambahan page dari coolify</h1>
    <h2>Hello World from Coolify!</h2>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0')
