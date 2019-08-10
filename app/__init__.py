from flask import Flask
from flask_mail import Mail


def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    
    Args:
        config_name : name of the configuration to be used
    '''
# Initialising application
app = Flask(__name__)

# Creating the app configurations
app.config.from_object(config_options[config_name])