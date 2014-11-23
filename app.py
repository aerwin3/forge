from forge import app
from forge.models import init_db

init_db()
app.run(debug=True)

