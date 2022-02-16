# Alfalfa Client (Newer Pandas Support)

The purpose of this branch is to test Alfalfa Client to support newer version of Pandas, to ensure the compatibility with Building-Controls-Simulator (https://github.com/ecobee/building-controls-simulator)
The list of modifications:
 - Changed the Pandas version from 0.24.2 to 1.2.4
 - Changed the Python version to 3.8.9
 - Fixed the issue when using alfalfa-client inside a docker container (e.g., Jupyter notebook) to Alfalfa deployed on localhost (of the host machine): see https://github.com/NREL/alfalfa-client/issues/20#issue-1131706037
 - *Warning*: This is an experimental branch for Whole Energy Home project, with potential bugs.
 
Original README below.


# Alfalfa Client

The purpose of this repository is to provide a standalone client for use with the Alfalfa application.  It additionally includes a Historian to quickly/easily enable saving of results from Alfalfa simulations.

# Usage

This repo is packaged and hosted on [PyPI here](https://pypi.org/project/alfalfa-client/).

```bash
pip install alfalfa-client
```

```python
import alfalfa_client.alfalfa_client as ac
import alfalfa_client.historian as ah

client = ac.AlfalfaClient
historian = ah.Historian
```

# Setup and Testing
This repository is setup to use:
- [pyenv](https://github.com/pyenv/pyenv#installation) for managing python versions
- [poetry](https://python-poetry.org/docs/#installation) for managing environment
- [pre-commit](https://pre-commit.com/#install) for managing code styling
- tox for running tests in isolated build environments.  See the expected python versions in [tox.ini](./tox.ini)

Assuming poetry is installed and the necessary python versions are installed, the following should exit cleanly:
```bash
git clone https://github.com/NREL/alfalfa-client.git
cd alfalfa-client
poetry run tox
```

This may take some time resolving on the initial run, but subsequent runs should be faster.

See [this gist](https://gist.github.com/corymosiman12/26fb682df2d36b5c9155f344eccbe404) for additional info.


# History
- The implemented client is previously referred to as Boptest, from the alfalfa/client/boptest.py implementation.  It has been ported as a standalone package for easier usage across projects.

# Releasing
See [release info here](https://gist.github.com/corymosiman12/26fb682df2d36b5c9155f344eccbe404#releasing)
