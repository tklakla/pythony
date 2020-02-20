#!flask/bin/python
from hello_world import app
app.run(host='127.0.0.1', port=5000, debug=True)