import configparser
import os


def LoadConfiguration():
    wkDbHost: str = '127.0.0.1'
    wkDbPort: str = '5432'
    wkDbUser: str = 'postgres'
    wkDbPassword: str = 'postgres'
    wkDbName: str = 'white_knight'

    # Get configuration from environment variables if they exist
    if 'WK_DB_HOST' in os.environ:
        wkDbHost = os.environ['WK_DB_HOST']

    if 'WK_DB_PORT' in os.environ:
        wkDbPort = os.environ['WK_DB_PORT']

    if 'WK_DB_USER' in os.environ:
        wkDbUser = os.environ['WK_DB_USER']

    if 'WK_DB_PASSWORD' in os.environ:
        wkDbPassword = os.environ['WK_DB_PASSWORD']

    if 'WK_DB_NAME' in os.environ:
        wkDbName = os.environ['WK_DB_NAME']

    config = configparser.ConfigParser()
    config['DATABASE'] = {'host': wkDbHost,
                        'port': wkDbPort,
                        'user': wkDbUser,
                        'password': wkDbPassword,
                        'database': wkDbName}
    return config

    