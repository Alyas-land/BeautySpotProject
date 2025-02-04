import os
from config import app, db

@app.before_request
def createDatabase():
    db.create_all()

if(__name__ == '__main__'):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.run(debug=True)

