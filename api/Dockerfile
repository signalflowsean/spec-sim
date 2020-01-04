FROM python:3.7.5-slim

WORKDIR  "/app"

# Copy the list of dependencies to the working directory of the container
COPY requirements.txt .

# update pip
RUN pip install --upgrade pip

# Build the dependencies
RUN pip install -r requirements.txt

# Copy over the rest of the files
# We copy twice to utilize layer caching https://docs.semaphoreci.com/article/81-docker-layer-caching
COPY . . 

# Run the flask app on start
CMD ["flask", "run"]

