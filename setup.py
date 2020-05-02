# Third Party --------------------------------------------------------------------------
from setuptools import setup


# This minimal package configuration is solely meant to make the module
# installable for use in the action Docker container and not to publish
# it on PyPi.
setup(
    name="kaggle_graph",
    install_requires=[
        "kaggle==1.5.6",
        "python-dotenv==0.13.0",
        "pandas==1.0.3",
        "seaborn==0.10.1",
        "matplotlib==3.2.1",
    ],
)
