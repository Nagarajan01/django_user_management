## Creating and Activating a Virtual Environment
Before you start working on this project, it's essential to set up a virtual environment. A virtual environment is a self-contained Python environment that isolates your project's dependencies from the system-wide Python installation. This helps maintain a clean and consistent environment for your project.
To create a virtual environment, open a terminal and navigate to your project directory. Run the following command to create a virtual environment named 'env':

```bash
virtualenv env
python -m venv env
.\env\Scripts\activate
source env/bin/activate
To deactivate the virtual environment, simply run the following command in your terminal:

```bash
deactivate
Using a virtual environment is a best practice in Python development, and it ensures that your project runs smoothly without conflicts. Make sure to activate the virtual environment every time you work on this project.
