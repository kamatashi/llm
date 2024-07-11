FROM python:3.10.12

# Set the working directory in the container
WORKDIR /llm

# Copy the application files into the working directory
COPY . /llm

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "app.py"]