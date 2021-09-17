# PythonExampleProject
A simple python project to demonstate how to set up a project from scratch with unit tests using vscode

# Quick setup instructions
Setting up a blank project
1. Initialise the virtual environment from vscode terminal \
 ```python -m venv ./venv```
2. Configure automatic virtual environment initialisation
  - Via vscode command pallet (Ctrl+shift+P): \
  ``` Python: select interpreter > Enter interpreter path > Find ```
  -  Now in your project you will see .vscode directory created. Open settings.json inside of it and add: \
    `"python.terminal.activateEnvironment": true`
3. Install project dependencies from requirements.txt
`python -m pip install -r requirements.txt`

## Package management
Once the project is set up with a virtual environment it is ready for development and we can begin to install packages with pip from the terminal.
For this example the requests package will be installed. To do this run the following command from vscode terminal: \
```pip install requests``` \
If installation is successful the package should be visable in `C:\\{projectpath}\venv\Lib\requests`

To Install project dependencies from requirements.txt \ 
`python -m pip install -r requirements.txt` \ 

To modify the requirements.txt run the following commmand: \
`(venv) PS C:\xxx\CHATool> pip freeze > requirements.txt` \

# Tests
## Setting up test runner with vscode
1. From vs command pallet (Ctrl+shift+P) \
```Python: Configure Tests > pytest > tests``` \
2. Next on the command pallet use the following command. This should load the vscode Test Explorer in the right hand pannel. Its icon is a test flask\
 ``` Python: Discover Tests``` \ 
3. Run Tests! \
 A. To run Run tests simply click the Run Tests button in the Test Explorer. \
 OR \
 B. Alternatively tests can be run from the terminal. All tests can be run with the following command. \
```python -m pytest``` \
 To run just a specifc test specify a path to the test file like so: \
```python -m pytest tests/sometestfile.py ``` \

# Info for beginners
## Virtual environments
To keep the projects python packages (code libraries) segrated from the global python packages we use a virtual environment.
This keeps python packages stored in a folder local to the project as opposed to the global bin/ folder.
This also means when updating a package in one python project, it does not impact same package used in another project
for more info see https://code.visualstudio.com/docs/python/environments
