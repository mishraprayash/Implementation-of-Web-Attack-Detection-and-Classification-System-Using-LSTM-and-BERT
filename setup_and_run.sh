#!/bin/bash

ENV_NAME="test_env"
YML_FILE="environment.yml"

# Check if Conda is installed
if ! command -v conda &>/dev/null; then
    echo "Conda not found. Please install Conda first."
    exit 1
fi

# Initialize Conda for the current shell session
eval "$(conda shell.bash hook)"

# Create the environment from the YAML file
echo "Creating Conda environment '$ENV_NAME' from '$YML_FILE'..."
conda env create -f "$YML_FILE"

# Activate the Conda environment
conda activate "$ENV_NAME"

if [[ $? -eq 0 ]]; then
    echo "Environment '$ENV_NAME' activated successfully."
else
    echo "Failed to activate environment '$ENV_NAME'."
    exit 1
fi

# Rest of your script
SCRIPT_DIR=$(pwd)
echo "Environment setup complete!"

# Check if Conda environment is activated
if [[ -z "$CONDA_DEFAULT_ENV" || "$CONDA_DEFAULT_ENV" != "$ENV_NAME" ]]; then
    echo "Activating Conda environment '$ENV_NAME'..."
    conda activate "$ENV_NAME"

    if [[ $? -ne 0 ]]; then
        echo "Failed to activate the Conda environment."
        exit 1
    fi
else
    echo "Environment '$ENV_NAME' is already activated."
fi

# Navigate to the app directory and run the Uvicorn server
cd "$SCRIPT_DIR/app"
echo "Starting the FastAPI server with Uvicorn..."
uvicorn main:app --reload

if [[ $? -eq 0 ]]; then
    echo "Server is running at http://localhost:8000"
else
    echo "Failed to start the server."
    exit 1
fi
