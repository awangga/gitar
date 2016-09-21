# Gitar
git auto remote, webhook for auto remote server including deploy, remove, delete. etc.

## Requirement
 * paramiko
 * virtualenv
 * uwsgi
 * nginx

### Instalation
```sh
# sudo apt-get install build-essential libssl-dev libffi-dev python-pip python-dev nginx
# pip install paramiko
# pip install virtualenv
# pip install uwsgi
```

### Setup
Direktory

```sh
$ mkdir gitar
$ cd gitar
$ virtualenv gitarenv
$ source mygitar/bin/activate
$ deactivate
```

uwsgi

```sh
$ sudo cp gitar.conf /etc/init/
$ sudo start gitar
```

nginx

```sh
server {
    listen 80;
    server_name gitar.vas.web.id;

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/devops/gitar/gitar.sock;
    }
}
```
