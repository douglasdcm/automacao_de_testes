FROM jenkins/jenkins:2.452.2-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
# RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
# https://download.docker.com/linux/debian/gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) \
#   signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
#   https://download.docker.com/linux/debian \
#   $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
# RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install -y pip
RUN apt install -y python3.11-venv
RUN apt install wget -y
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/libu/libu2f-host/libu2f-udev_1.1.4-1_all.deb
RUN dpkg -i libu2f-udev_1.1.4-1_all.deb
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install xdg-utils -y
RUN apt install libxkbcommon-x11-0 -y
RUN apt-get install libxdamage1 -y
RUN apt-get install libvulkan1 -y
RUN apt-get install libpangocairo-1.0-0 -y
RUN apt-get install libnss3-dev -y
RUN apt-get install libasound2 -y
RUN apt-get install libatk1.0-0 -y
RUN apt-get install libglib2.0-dev -y
RUN apt-get install fonts-liberation -y
RUN echo "deb http://deb.debian.org/debian bookworm-backports main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install libatspi2.0-0 -y
RUN apt-get install libatk-bridge2.0-0 -y
RUN apt-get install libcups2 -y
RUN apt install libgtk-3-dev -y
RUN apt-get install libgtk-4-1 -y
# RUN dpkg -i google-chrome-stable_current_amd64.deb
ADD . .
RUN dpkg -i google-chrome-stable_current_amd64.deb
USER jenkins
# RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"