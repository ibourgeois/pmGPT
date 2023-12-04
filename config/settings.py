""" Settings for the application. """
from cli.utils.helper_functions import get_env_variable

DATABASE_PATH = get_env_variable(
    'DATABASE_PATH', 
    default = 'database.db',
    help_message = "Enter the path to the database file:"
)

OPENAI_API_KEY = get_env_variable(
    'OPENAI_API_KEY', 
    help_message = "You can find your API key at https://beta.openai.com/account/api-keys"
)