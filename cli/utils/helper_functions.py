""" Helper functions for the CLI """
import os
from pathlib import Path
import click
from dotenv import load_dotenv, set_key

# Load the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def get_env_variable(var_name, default=None, help_message=None):
    """ Get the environment variable or prompt the user for it. """
    # Try to fetch the variable from the environment
    value = os.getenv(var_name)
    if value is None:
        if help_message:
            click.echo(help_message)
        try:
            # Variable not found; prompt the user for the value
            value = click.prompt(f"Enter the value for {var_name}", default=default)
            # Save the variable for future runs
            set_key(env_path, var_name, value)
            # Reload the .env file to update the environment variables
            load_dotenv(dotenv_path=env_path)
        except click.Abort:
            # The user cancelled the prompt (e.g. with CTRL-C)
            click.echo(f"\nInput cancelled. Using default value for {var_name}.")
            # Use the default value if the user cancels the prompt
            if default:
                value = default
                # Save the variable for future runs
                set_key(env_path, var_name, value)
                # Reload the .env file to update the environment variables
                load_dotenv(dotenv_path=env_path)
    return value
