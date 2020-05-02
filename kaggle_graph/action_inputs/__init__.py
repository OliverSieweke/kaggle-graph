"""
Action Inputs
=============

This module contains utility methods for retrieving action inputs from
the environment.
"""

# Standard Library ---------------------------------------------------------------------
import os

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv


input_schema = {
    "KAGGLE_USERNAME": str,
    "KAGGLE_KEY": str,
    "KAGGLE_COMPETITION_ID": str,
    "GRAPH_NAME": str,
    "Y_MIN": float,
    "Y_MAX": float,
    "OBJECTIVE": float,
    "SCORE": str,
}


def get_action_inputs() -> dict:
    """Return a dictionary containing all action inputs.

    .. note::
     This method further loads the Kaggle credentials into
     the environment.

    Returns
    -------
    :code:`dict`
        Dictionary containing all action inputs.

    Example
    -------
    >>> get_action_inputs()
    {'KAGGLE_USERNAME': 'oliversieweke',
     'KAGGLE_KEY': '***',
     'KAGGLE_COMPETITION_ID': 'titanic',
     'GRAPH_NAME': None,
     'Y_MIN': 0,
     'Y_MAX': 1,
     'OBJECTIVE': 0.8,
     'SCORE': 'positive'}
    """
    load_dotenv()

    action_inputs = {
        key: (cast(os.getenv(f"INPUT_{key}")) if os.getenv(f"INPUT_{key}") else None)
        for (key, cast) in input_schema.items()
    }

    # Loading Kaggle credentials into the environment:
    os.environ["KAGGLE_USERNAME"] = action_inputs["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = action_inputs["KAGGLE_KEY"]

    return action_inputs
