from flask import Flask

app = Flask(__name__)

import forge.resources
import models


@app.teardown_appcontext
def shutdown_session(exception=None):
    models.db_session.remove()