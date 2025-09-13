# Step 1: Start with an official, lightweight Python base image
FROM python:3.9-slim

# Step 2: Set a working directory inside the container
# All subsequent commands will run from here.
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install the Python dependencies
# This runs INSIDE the container during the build process.
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy your application code and necessary data artifacts
# We copy the 'api' folder, and the 'processed_data' folder which has the preprocessor.
COPY ./api ./api
COPY ./processed_data ./processed_data
COPY ./models ./models

# Step 6: Define the command that will run when the container starts
# This tells the container to start the Uvicorn server.
# We use "--host 0.0.0.0" to make it accessible from outside the container.
CMD ["uvicorn", "api.serve_model:app", "--host", "0.0.0.0", "--port", "8000"]