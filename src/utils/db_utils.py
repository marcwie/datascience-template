"""
Helper functions to connect to a postgres data base.
"""
import os
import numpy as np
from dotenv import load_dotenv
import psycopg2
import pandas as pd


def connector():
    """
    Establish connection to the a postgres data base.

    Requires that all environment variables are set in .env in the root of this repository.

    Returns:
        connection:
            The data base connector.
    """
    load_dotenv()

    conn = psycopg2.connect(**{
        "database": os.getenv("DBNAME"),
        "user": os.getenv("DBUSER"),
        "port": os.getenv("PORT"),
        "host": os.getenv("HOST"),
        "password": os.getenv("PASSWORD")
        }
    )

    return conn


def run_query(query):
    """
    Run an SQL query against a postgres database.

    Args:
        query (str):
            the SQL query to execute.

    Returns:
        pandas.DataFrame:
            The query results.
    """
    conn = connector()
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


def tuple_of_values(values):
    """
    Converts a given value or list of values to a format that can be
    inserted into IN statements of an SQL query.

    Ensures that the IN-condition for SQL queries either takes the form
    '(value)' in the case of a single requested user id or '(value1, value2,
    ..., valueN)' in the case of multiple requested values.

    Args:
        values (int, list, or array):
            Values that are inserted into the SQL queries.

    Returns:
        tuple or string:
            Tuple containing all values.
    """
    if isinstance(values, int) or isinstance(values, np.int64):
        formatter = f'({values})'
    elif len(values) == 1:
        formatter = f'({values[0]})'
    else:
        formatter = tuple(values)

    return formatter
