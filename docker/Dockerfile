FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

# Apt updates
RUN 	apt-get update \
	&& apt-get install -y \
		build-essential \
		zlib1g-dev \
		git \
		libreadline-gplv2-dev \
		libncursesw5-dev \
		libssl-dev \
		libsqlite3-dev \
		tk-dev \
		libgdbm-dev \
		libc6-dev \
		libbz2-dev \
		tmux \
		wget \
		python3-tk

# Install python 3.6
RUN wget https://www.python.org/ftp/python/3.8.11/Python-3.8.11.tar.xz \
	&& tar xvf Python-3.8.11.tar.xz \
	&& cd Python-3.8.11 \
	&& ./configure --with-zlib=/usr/include \
	&& make \
	&& make install \
	&& ln -s /usr/local/bin/python3 /usr/local/bin/python \
	&& ln -s /usr/local/bin/pip3 /usr/local/bin/pip

# Install project-specific python libraries
RUN pip install gym matplotlib opencv-python lz4 psutil flake8 ray
# tensorflow-gpu==1.12.0

# Symlinking for making ray work
RUN rm -r /usr/local/lib/python3.6/site-packages/ray/rllib \
	&& ln -s /ray/python/ray/rllib /usr/local/lib/python3.6/site-packages/ray/rllib \
	&& rm -r /usr/local/lib/python3.6/site-packages/ray/tune \
	&& ln -s /ray/python/ray/tune /usr/local/lib/python3.6/site-packages/ray/tune



WORKDIR /project
