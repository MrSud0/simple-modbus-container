# Modbus Server Project

## Description

This project is a Modbus server built with Python. It uses the `pymodbus` library to create a Modbus TCP server. The server is designed to run inside a Docker container.

## Project Structure

- `Dockerfile`: Defines the Docker image for the Modbus server.
- `entrypoint.sh`: The entry point script that starts the Modbus server.
- `modbus-server.py`: The main Python script for the Modbus server.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Prerequisites

- Docker
- Python 3.8+

## Getting Started

### Build the Docker Image

To build the Docker image, run the following command in the project directory:

```sh
docker build -t modbus-server .
```

### Run the Docker Container

To run the Docker container, use the following command:

```sh
docker run -d -p 5020:5020 modbus-server
```

This will start the Modbus server and map port 5020 of the container to port 5020 on your host machine.

### Accessing the Modbus Server

The Modbus server will be accessible at `localhost:5020`. You can connect to it using any Modbus client.

## Python Dependencies

The project requires the following Python packages:

- `pymodbus==3.6.8`
- `asyncio==3.4.3`

These dependencies are listed in the `requirements.txt` file and are installed during the Docker image build process.

## Scripts

### `modbus-server.py`

This is the main script that initializes and runs the Modbus server. It leverages the `pymodbus` library to handle Modbus TCP communications.

### `entrypoint.sh`

This shell script serves as the entry point for the Docker container. It simply runs the `modbus-server.py` script:

```sh
#!/bin/sh
python /usr/src/app/modbus-server.py "$@"
```

## Dockerfile

The `Dockerfile` is used to create the Docker image for the project. Below is a brief explanation of each step:

1. **Base Image**: Uses the official Python 3.8 image.
2. **Set Working Directory**: Sets the working directory to `/usr/src/app`.
3. **Copy Files**: Copies the project files into the container.
4. **Install Dependencies**: Installs the required Python packages using `pip`.
5. **Set Entrypoint**: Specifies `entrypoint.sh` as the entry point script.

```Dockerfile
# Use official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5020 available to the world outside this container
EXPOSE 5020

# Run entrypoint.sh when the container launches
ENTRYPOINT ["sh", "entrypoint.sh"]
```

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
