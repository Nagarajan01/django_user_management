## Creating and Activating a Virtual Environment

Before you start working on this project, it's essential to set up a virtual environment. A virtual environment is a self-contained Python environment that isolates your project's dependencies from the system-wide Python installation. This helps maintain a clean and consistent environment for your project.

To create a virtual environment, open a terminal and navigate to your project directory. Run the following command to create a virtual environment named 'env':

For Windows:

```bash
virtualenv env
```
For Linux:
```bash
python -m venv env
```
For activation:
```bash
.\env\Scripts\activate  #windows
source env/bin/activate  #linux
```
To deactivate the virtual environment, simply run the following command in your terminal:
```bash
deactivate
```
To install the project's dependencies from the requirements.txt file within the virtual environment, use the following command

```bash
pip install -r requirements.txt
```

## Using Docker for Development

### Creating Docker Files

To containerize your project for development, you'll need to create two essential Docker files:

1. **Dockerfile**: This file contains the necessary instructions to build a Docker image for your Django project.

2. **docker-compose.yml**: This file contains the configuration for your Django application and any related services (e.g., a database).

### Building Docker Images

To build Docker images for your project and its services, use the following command:

```bash
docker compose up -d   # This builds all images configured in the docker-compose.yml file
```
When there is a change only in one of the services, for eg: API code base, run:
```bash
docker compose up -d --no-deps  # This rebuilds only the service in which changes are made.
```
To check logs use the following commands:

```bash
docker logs pp-web-1 -tf  # for API logs
docker logs pp-celery-beat-1 -tf  # for background process logs
```




