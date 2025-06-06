# Flask
Task-Flask Application

Server:
sudo apt update && sudo apt upgrade -y

Install java:
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version
openjdk version "21.0.3" 2024-04-16
OpenJDK Runtime Environment (build 21.0.3+11-Debian-2)
OpenJDK 64-Bit Server VM (build 21.0.3+11-Debian-2, mixed mode, sharing)


Install jenkins :
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

sudo apt install python3-venv -y

Create Venv & Activate:
python3 -m venv venv
source venv/bin/activate

Install Flask:
pip install Flask

Install Gunicorn:
pip install gunicorn

Install apache2:
sudo apt install apache2 -y

Install mod_wsgi for Apache (to serve Flask apps):
sudo apt install libapache2-mod-wsgi-py3 -y
sudo a2enmod wsgi
sudo systemctl restart apache2


infinitydeploy.cloud.conf (APACHE CONFIG FILE):

<VirtualHost *:80>
    ServerName infinitydeploy.cloud
    ServerAlias www.infinitydeploy.cloud

    DocumentRoot /home/ubuntu/Flask
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/


    <Directory /home/ubuntu/Flask>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/infinitydeploy.cloud-error.log
    CustomLog ${APACHE_LOG_DIR}/infinitydeploy.cloud-access.log combined
</VirtualHost>


IN VSC :
git init

git remote add origin https://github.com/Hariprasath76/Flask.git

git add .
git commit -m "Initial commit"
git branch -M main 
git push -u origin main

Jenkins Pipelines:

pipeline {
    agent any

    environment {
        REMOTE_USER = "ubuntu"
        REMOTE_HOST = "15.207.115.229"
        REMOTE_PATH = "/home/ubuntu/Flask"
        IMAGE_NAME = "hari760/infinitydeploy"
        IMAGE_TAG = "v1.0"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Hariprasath76/Flask.git', branch: 'main'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['Flask']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                            cd "${REMOTE_PATH}" &&
                            git pull origin main
                        '
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sshagent(['Flask']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                            cd "${REMOTE_PATH}" &&
                            docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
                        '
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sshagent(['Flask']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                            CONTAINER_ID=\$(docker ps -q --filter ancestor="${IMAGE_NAME}:${IMAGE_TAG}")
                            if [ ! -z "\$CONTAINER_ID" ]; then
                                docker stop "\$CONTAINER_ID" || true
                                docker rm "\$CONTAINER_ID" || true
                            fi

                            docker run -d -p 5000:5000 "${IMAGE_NAME}:${IMAGE_TAG}"
                        '
                    """
                }
            }
        }
    }
}



generate the Key for server access -> Jenkins .
 ssh-keygen -t rsa -b 4096 -C "jenkins@ec2"
 cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa


Add private ->jenkins .
add public key -> authorized_keys

sudo apt update
sudo apt install libapache2-mod-wsgi-py3 -y

sudo nano /etc/systemd/system/flaskapp.service
[Unit]
Description=Gunicorn instance to serve Flask App
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/Flask
Environment="PATH=/home/ubuntu/Flask/venv/bin"
ExecStart=/home/ubuntu/Flask/venv/bin/gunicorn --workers 1 --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl start flaskapp
sudo systemctl status flaskapp
sudo systemctl enable flaskapp



Create Docker File:

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (if any)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port the app runs on
EXPOSE 5000

# Command to run the Flask app (adjust if you use gunicorn or something else)
CMD ["python", "app.py"]

install Docker:
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
docker build -t infinitydeploy/flaskapp:latest .

sudo sudo docker run -p 5000:5000 infinitydeploy/flaskapp:latest

docker image ->docker hub:
docker login -u hari760
password:


sudo docker images
sudo docker push hari760/infinitydeploy:latest

sudo usermod -aG docker $USER
newgrp docker 

docker tag 0709a7387aa4 docker.io/hari760/infinitydeploy:v1.0
docker push hari760/infinitydeploy:v1.0

