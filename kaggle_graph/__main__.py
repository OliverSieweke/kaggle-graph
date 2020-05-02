# Third Party --------------------------------------------------------------------------
from kaggle_graph.action_inputs import get_action_inputs
from kaggle_graph.plot import kaggle_submission_scores
from kaggle_graph.submissions import fetch, parse


# Load action inputs:
action_inputs = get_action_inputs()


# Generate and save Kaggle graph:
kaggle_submission_scores(
    parse(fetch(action_inputs["KAGGLE_COMPETITION_ID"])),
    graph_name=action_inputs["GRAPH_NAME"],
    ymin=action_inputs["Y_MIN"],
    ymax=action_inputs["Y_MAX"],
    objective=action_inputs["OBJECTIVE"],
    score=action_inputs["SCORE"],
)
