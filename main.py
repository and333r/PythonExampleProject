#Project initialisation - Setting up virtual environment
#To keep the projects python packages segrated from the global python packages we use a virtual environment
#This keeps python package stored in a bin/ folder local to the project as opposed to the global  bin folder.
#This also means when updating a package in one python project, it does not impact same package used in another project
#for more info see https://code.visualstudio.com/docs/python/environments

#To initialise the virtual environment use the following command in the terminal 
#python -m venv C:\{path to project}
#python -m venv C:\Users\dylan\Documents\Src\ExamplePythonProject\venv

#Package management
#Once the project is isolated and ready for development to begin we install packages with pip from the terminal.
#Before we do this we need to make sure we activate the virtual envrionment from our terminal so that any commands we run in the terminal
#are ran from the context of our virtual environment
#To do this on windows :
#   navigate run the following script from the vscode terminal C:\{path to project}\venv\Scripts\Activate.ps1
#To do this on linux:
#   navigate run the following script from the vscode terminal C:\{path to project}\venv\bin\Activate.???
#In vscode the terminal should not change from :
#PS C:\Users\dylan\Documents\Src\ExamplePythonProject\venv\Scripts>
#to:
#(venv) PS C:\Users\dylan\Documents\Src\ExamplePythonProject\venv\Scripts> 

#Install a package (finally)
#For this example the requests package will be installed. To do this run the following command:
# (venv) PS C:\Users\dylan\Documents\Src\ExamplePythonProject\venv\Scripts> pip install requests
# If installation is successful the package should be visable in {projectpath}\venv\Lib\requests

#Put main code in here
#



#