# Import db from app factory
from app import create_app,db
from flask_script import Manager,Server
# Connect to models
from app.models import User,Blog,Comment
# Set up migrations
from flask_migrate import Migrate,MigrateCommand