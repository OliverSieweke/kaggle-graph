"""
Plot
====

This module contains methods for generating and saving graphs of Kaggle
submission scores.
"""

# Standard Library ---------------------------------------------------------------------
from typing import Optional

# Third Party --------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, DayLocator

# Data Science
import pandas as pd


def kaggle_submission_scores(
    submissions_df: pd.DataFrame,
    graph_name: Optional[str] = "kaggle-submissions-graph",
    ymin: Optional[float] = None,
    ymax: Optional[float] = None,
    objective: Optional[float] = None,
    score: Optional[str] = "positive",
) -> None:
    """Save plot of Kaggle submission scores.

    Parameters
    ----------
    submissions_df
        Submissions data frame
    graph_name: optional
        Name of the graph image file to be saved (defaults to
        :code:`"kaggle-submissions-graph"`).
    ymin: optional
        Y-axis mimumium boundary (set automatically if not provided).
    ymax: optional
        Y-axis maximum boundary (set automatically if not provided).
    objective: optional
        Score objective, to be displayed on the graph (defaults
        to :code:`None`).
    score: optional
        Specifies whether the objective is to :code:`"maximize"` or
        :code:`"minimize"` the score (defaults to :code:`"maximize"`)

    Returns
    -------
    None
        While nothing is returned, a plot of the Kaggle submission
        scores is saved, under :code:`f"./{graph_name}.png"`.

    Note
    ----
    This function is intended to be used in conjunction with
    :meth:`kaggle_graph.submissions.parse`.

    Example
    -------
    >>> from kaggle_graph.submissions import fetch, parse
    >>> kaggle_submission_scores(parse(fetch("titanic")))
    """
    if graph_name is None:
        graph_name = "kaggle-submissions-graph"

    # Clean and Sort Data
    submissions_df.dropna(subset=["publicScore"], inplace=True)
    submissions_df.sort_values(by=["date"], inplace=True)

    # Graph
    sns.set()
    g = sns.lineplot(x="date", y="publicScore", data=submissions_df, marker="o")

    # Title and Labels
    g.set(title="Kaggle", xlabel="Date", ylabel="Public Score")
    g.xaxis.set_major_locator(DayLocator(interval=1))
    g.xaxis.set_major_formatter(DateFormatter("%d %b %y"))

    # Boundaries
    if ymin is not None:
        plt.ylim(ymin=ymin)
    if ymax is not None:
        plt.ylim(ymax=ymax)

    # Color Areas
    if score is None:
        score = "positive"
    plt.fill_between(
        submissions_df["date"], submissions_df["publicScore"], color="b", alpha=0.3
    )
    if objective:
        g.axhline(objective, ls="-", color="r", alpha=0.3)
        plt.fill_between(
            submissions_df["date"],
            submissions_df["publicScore"],
            objective,
            where=submissions_df["publicScore"] < objective,
            interpolate=True,
            color="g" if score == "negative" else "r",
            alpha=0.3,
        )
        plt.fill_between(
            submissions_df["date"],
            objective,
            submissions_df["publicScore"],
            where=objective <= submissions_df["publicScore"],
            interpolate=True,
            color="r" if score == "negative" else "g",
            alpha=0.3,
        )

    # Save
    graph_file_name = f"{graph_name}.png"

    plt.savefig(
        graph_file_name,
        # Prevent labels to be cut off in saved image:
        bbox_inches="tight",
    )
