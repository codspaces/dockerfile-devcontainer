# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container to /app
WORKDIR /app

# Clone the PyTorch repository
RUN git clone https://github.com/pytorch/pytorch.git

WORKDIR /app/pytorch