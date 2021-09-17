# PythonExampleProject
A simple python project to demonstate how to set up a project from scratch with unit tests using vscode

# Quick setup instructions
Setting up a blank project
1. Initialise the virtual environment from vscode terminal \
 ```python -m venv ./venv```
2. Configure automatic virtual environment initialisation
  - Via vscode command pallet: \
  ``` Python: select interpreter > Enter interpreter path > Find ```
  -  Now in your project you will see .vscode directory created. Open settings.json inside of it and add: \
    `"python.terminal.activateEnvironment": true`

# Some theory
## Project initialisation - Setting up virtual environment
To keep the projects python packages (code libraries) segrated from the global python packages we use a virtual environment.
This keeps python packages stored in a folder local to the project as opposed to the global bin/ folder.
This also means when updating a package in one python project, it does not impact same package used in another project
for more info see https://code.visualstudio.com/docs/python/environments

## Package management
Once the project is set up with a virtual environment it is ready for development and we can begin to install packages with pip from the terminal.
For this example the requests package will be installed. To do this run the following command from vscode terminal: \
```pip install requests``` \
If installation is successful the package should be visable in C:\{projectpath}\venv\Lib\requests
