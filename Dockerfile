#Use an official Python runtime as parent image
FROM python:3.10.0

#Set environment variables for Python to not buffer output
ENV PYTHONBUFFERED 1

#Set the working directory in the container
WORKDIR /app

#Copy the current directory contents into the container at /app
COPY . /app/

#Install poetry and use poetry to install all the dependencies in the poetry.lock file
RUN pip install poetry
RUN poetry install

#Expose the port that Django runs on
EXPOSE 8000

#Run Django's development server
CMD CMD ["gunicorn", "--bind", "0.0.0.0:8000", "waitlist.wsgi:application"]