FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# Install Python
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev ffmpeg gnupg curl git && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
RUN nvm install 18 && nvm use 18
RUN npm install @openapitools/openapi-generator-cli -g && npm install -g ng-openapi-gen