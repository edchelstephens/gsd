import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def index():
    count = get_hit_count()
    html ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Compose</title>
    </head>
    <body>
        <main>
            <h1 style="font-weight:bold;color:green"><code>Dodot Tries Docker Compose!</code></h1>
            <p style="font-weight:bold; color:darkgreen">Hit refresh if you think Django is the best web framework in the world!</p>
            <br/>
            <p style="font-weight:bold; color:darkgreen">You've only refreshed {} times. REFRESH MORE!!!\n</p>
        
        </main>
    </body>
    </html>
    """.format(count)
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
