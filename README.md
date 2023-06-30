## Blob Reader App 

This application serves a flask web app through nginx reverse proxy. 
Both flask app and the reverse proxy is hosted in Azure vm.

## Installation

1. Install `docker` in the vm.

```console
#vm> sudo apt-get update
#vm> sudo apt-get install docker.io
```

2. Download the `flask-nginx-image.tar` from the releases.

```console
#vm> curl -L https://github.com/sarath-srinivas/mle-cloud-training/releases/download/v0.0.1/flask-nginx-image.tar > flask-nginx-image.tar
```

3. Load the image into `docker`.

```console
#vm> sudo docker load -i flask-nginx-image.tar
```

4. Clone(or copy) the repository.

```console
#vm> git clone git@github.com:sarath-srinivas/mle-cloud-training.git
```

5. Run the docker container with bind mount attached to `blob_reader_app`.

```console
#vm> cd mle-cloud-training/
#vm> sudo docker run -d -p 80:80 -v $PWD/blob_reader_app:/app flask-nginx:v1
```

Then the flask app will be served in port 80 in the ip address of the vm.

