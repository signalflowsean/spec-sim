from api import create_app, db
from api.models import User, View

app = create_app()

# creates a shell context that adds the database instance and models to the shell session
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'View': View } 