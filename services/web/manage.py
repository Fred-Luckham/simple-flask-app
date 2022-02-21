# Imports
from flask.cli import FlaskGroup
from project import app, db

# Define app
cli = FlaskGroup(app)

# Recreate the DB
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()