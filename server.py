import sentry_sdk
import os
from bottle import Bottle, request, route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://07c92891bb8749ccbda5d4e34505f8cf@o399508.ingest.sentry.io/5256758",
    integrations=[BottleIntegration()]
)


@route('/')  
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>info</title>
  </head>
  <body>
    <div class="container">
      <p>Это главная страничка.</p>
    </div>
  </body>
</html>
"""
    return html  

@route('/success')  
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Страничка, где всё работает!!!</title>
  </head>
  <body>
    <div class="container">
      <h1>Все работает!</h1>
    </div>
  </body>
</html>
"""
    return html  

@route('/fail')  
def index():  
    raise RuntimeError("There is an error!")  
    return  
  
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)