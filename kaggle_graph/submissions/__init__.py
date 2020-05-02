"""
Submissions
===========

This module contains methods for fetching and parsing submissions to
`Kaggle Competitions`_.

.. _Kaggle Competitions: https://www.kaggle.com/competitions
"""

# Standard Library ---------------------------------------------------------------------
import subprocess
from io import StringIO

# Data Science
import pandas as pd


class KaggleError(Exception):
    """Raised when a Kaggle API call exits with a non-zero error code."""

    ...


def fetch(competition_id: str) -> str:
    """Fetch submissions to the Kaggle competition.

    .. warning::

        This method relies on Kaggle credentials to be exposed under
        the environment variables:

          - :code:`KAGGLE_USERNAME`
          - :code:`KAGGLE_KEY`

    Parameters
    ----------
    competition_id
        Kaggle competition ID (can be read from the Kaggle competition
        URL).

    Returns
    -------
    :code:`str`
        Kaggle submissions table in CSV format.
        
        The table contains the following columns and associated types::

            fileName               date                 description        status    publicScore  privateScore
            ---------------------  -------------------  -----------------  --------  -----------  ------------
            gender_submission.csv  2020-04-27 10:56:14  Gender Submission  complete  0.76555      0.75443

    Raises
    ------
    KaggleError
        If the Kaggle API call fails.

    Example
    -------
    >>> fetch("titanic")
    fileName,date,description,status,publicScore,privateScore
    gender_submission.csv,2020-04-27 10:56:14,Gender Submission,complete,0.76555,None

    References
    ----------
    - `Kaggle API Credentials`_
    - `Kaggle Submissions API`_

    .. _Kaggle API Credentials: https://github.com/Kaggle/kaggle-api#api-credentials
    .. _Kaggle Submissions API: https://github.com/Kaggle/kaggle-api/#list-competition-submissions
    """
    result = subprocess.run(
        ["kaggle", "competitions", "submissions", "--csv", competition_id],
        capture_output=True,
    )

    if result.returncode == 1:
        output = str(result.stderr or result.stdout, "utf-8").replace("\n", "\n\t\t")
        raise KaggleError(
            f"Unexpected error in fetching Kaggle submissions:\n"
            f"\tReturn Code: {result.returncode}\n"
            f"\tOutput: {output}\n"
            "\tPlease verify the Kaggle competition ID and credentials "
            "provided in the environment"
        )
    elif result.returncode == 2:
        output = str(result.stderr or result.stdout, "utf-8").replace("\n", "\n\t\t")
        raise KaggleError(
            f"Misused Kaggle command in fetching submissions:\n"
            f"\tReturn Code: {result.returncode}\n"
            f"\tOutput:\n\t\t{output}\n"
            "\tPlease check the documentation: https://github.com/Kaggle/kaggle-api#kaggle-api"
        )
    else:
        return str(result.stdout, "utf-8")


def parse(kaggle_csv_submissions_table: str) -> pd.DataFrame:
    """

    Parameters
    ----------
    kaggle_csv_submissions_table
        Kaggle submissions table in CSV format.
        
        The table should contain the following columns and associated
        types::

            fileName               date                 description        status    publicScore  privateScore
            ---------------------  -------------------  -----------------  --------  -----------  ------------
            gender_submission.csv  2020-04-27 10:56:14  Gender Submission  complete  0.76555      0.75443


    Returns
    -------
    :code:`pd.DataFrame`
        Kaggle submissions data frame.

    Note
    ----
    This function is intended to be used in conjunction with :meth:`fetch`.

    Example
    -------
    >>> parse(fetch("titanic"))
                    fileName                date  ... publicScore privateScore
    0  gender_submission.csv 2020-04-27 10:56:14  ...     0.76555      0.75443
    """
    submissions_df = pd.read_csv(StringIO(kaggle_csv_submissions_table),)

    submissions_df["date"] = pd.to_datetime(
        submissions_df["date"], format="%Y-%m-%d %H:%M:%S"
    )
    submissions_df["publicScore"] = pd.to_numeric(
        submissions_df["publicScore"], errors="coerce"
    )
    submissions_df["privateScore"] = pd.to_numeric(
        submissions_df["privateScore"], errors="coerce"
    )

    return submissions_df
