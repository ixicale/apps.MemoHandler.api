# Docker file to build the image for API server
FROM python:3.9

# Install the required packages
COPY requirements.txt ./
RUN python3.9 -m pip install --upgrade pip && python3.9 -m pip install -r requirements.txt -t .

# Set the working directory
COPY . .
WORKDIR /app

# Run the API server
CMD ["python", "app.py"]

