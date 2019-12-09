# Use an official Python runtime as an image
FROM python:3.7

# Copy files to container
COPY newsfetcher /newsfetcher
COPY requirements.txt /
COPY main.py /

# Install any needed packages specified in requirements.txt
RUN pip install -r /requirements.txt

# Run app.py when the container launches
CMD [ "python", "main.py" ]
