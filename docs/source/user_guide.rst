User Guide
==========

.. include:: ../../README.rst
   :start-after: .. getting_started
   :end-before: .. before_notes

.. note::
  - The :code:`KAGGLE_KEY` key can be generated on Kaggle_ under ``My Profile
    > Edit Profile > API > Create New Api Token``.
  - The :code:`KAGGLE_USERNAME` can be found on Kaggle_ under ``My Profile > Edit
    Profile``.
  - The :code:`KAGGLE_COMPETITION_ID` can be read from the competition's URL.

.. note::
    **Kaggle Graph** is designed to be used in conjunction with the following
    GitHub actions:

      - checkout_
      - git-auto-commit_

.. include:: ../../README.rst
   :start-after: .. after_notes
   :end-before: .. before_references

Troubleshooting
---------------

- My graph does not update:
   GitHub seems to be caching images. Although the graph updates, the display
   may take a couple of minutes to reflect the change.

References
----------

  - `Creating and storing encrypted secrets`_
  - `Workflow syntax for GitHub Actions`_
  - `checkout action`_
  - `git-auto-commit action`_

.. _Kaggle: https://www.kaggle.com/
.. _`Creating and storing encrypted secrets`: https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets
.. _`Workflow syntax for GitHub Actions`: https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions
.. _checkout: https://github.com/actions/checkout
.. _git-auto-commit: https://github.com/stefanzweifel/git-auto-commit-action
.. _checkout action: https://github.com/actions/checkout
.. _git-auto-commit action: https://github.com/stefanzweifel/git-auto-commit-action
