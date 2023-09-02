#!/bin/bash
set -e

ctrl_c() {
    echo "** Trapped CTRL+C key is executed"
    exit 1
}

# Set up the trap
trap ctrl_c INT

# Executing and printing all the commands
execute_print_cmd() {
    echo "Executing: $1"
    eval $1
    if [[ $? -ne 0 ]]; then
        echo "Error while executing the command: $1"
        exit 1
    fi    
}

echo "Enter the name of the virtual environment you want to create"
read venv_name
execute_print_cmd "python3 -m venv $venv_name"

echo "Activating the virtual environment"
source "$venv_name/bin/activate"

echo "Enter your OpenAPI Key: "
echo "How to generate or find my OpenAPI key: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key"
read -s OPENAI_API_KEY
echo "Enter your AWS Access Key ID: "
echo "How to generate AWS ACCESS/SECRET key: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html"
read AWS_ACCESS_KEY_ID
echo "Enter your AWS Secret Access Key: "
read -s AWS_SECRET_ACCESS_KEY
echo ""
echo "Enter your AWS Default Region: "
read AWS_DEFAULT_REGION

export OPENAI_API_KEY=$OPENAI_API_KEY
export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION

echo "Installing all the dependencies"
execute_print_cmd "pip install -r requirements.txt"

echo "Starting the AWSGPT application"
execute_print_cmd "streamlit run awsgpt_app.py"
