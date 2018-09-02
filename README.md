# django-lab
A simple demonstration of a Django/PostGreSQL/EC2 deloyment.  Run time 
economy is the primary goal.  AWS RDS is nice, but managed services are 
pricey.  Many applications run well enough w/the database and web server 
on the same EC2 instance.  This post demonstrates a minimal deployment 
to AWS LINUX hosted on a EC2 server.  I will skip most of the AWS 
administration since it is thoroughly covered within the AWS documentation.

The django project is named "mvp" and consists of two simple applications 
("app1" and "app2") because I wanted to investigate navigating between 
multiple applications.

I will created an account "django" to hold the django application.  httpd 
(apache) will use uwsgi as a bridge to django.  "django" (the UNIX account) 
will need to be a member of the apache (UNIX) group.

## EC2 (deployment environment)

1.  Start an EC2 instance.  Original MVP development was on a t2.small 
instance using a LINUX2 AMI w/a 8GB EBS file system.

1.  Install these packages (as root)
    1. `yum -y groupinstall 'Development Tools'`
    1. `yum -y install python3 python3-devel httpd-devel`
    1. `yum -y install postgresql postgresql-server`

1.  Configure PostGreSQL
    1. `service postgresql initdb` (as root)
    1. edit /var/lib/pgsql/data/postgresql.conf
        1. enable a listener on localhost by uncommenting
            1. listen_addresses = 'localhost'
            1. port = 5432
    1. edit /var/lib/pgsql/data/pg_hba.conf
        1. trust users on the loopback
            1. local   all             all                                     trust
            1. host    all             all             127.0.0.1/32            trust
            1. host    all             all             ::1/128                 trust
    1. start postgresql 
        1.  `service postgresql start` (as root)
    1.  Verify postgres is working by logging in
        1. `psql -d template1 -U postgres`
        1. `\q` will exit

1.  Start httpd and ensure you can connect to it
    1. `service httpd start` (as root)
    1. visit your public IP address w/a browser, should see Apache test page
    1. edit /etc/httpd/httpd.conf

1.  Install virtualenv (as root)
    1. `pip3 install virtualenv`

1.  Create a LINUX user account 'django' to hold the project, and add to apache group
    1. `useradd -m django` (as root)
    1. `usermod -a -G apache django` (as root)
    1. `chown -R django:apache /var/www` (as root)
    1. `sudo chmod 2775 /var/www` (as root)

1.  su to django 
    1. pull sources from github
        1. `git clone https://github.com/guycole/django-lab.git`
    1. create postgresql user and database
        1. run postgres/genesis.sh (genesis.sql contains postgresql operations)
    1. verify happy postgres account and database creation
        1. `psql -U django -d mvp` (there are no tables yet)
        1. `\q` will exit
    1. establish virtualenv and seed environment
        1. `virtualenv -p /usr/bin/python3 venv`
        1. source venv/bin/activate
        1. `pip install -r requirements.txt`
        1. Check for happy django startup
            1. `python manage.py runserver` (Control C to exit)
        1. Run migrations and ensure ok database connection
            1. `python manage.py migrate`
        1. Edit mvp/settings.py and tweak ALLOWED_HOSTS to reflect your EC2 public IP
    1. build and install mod_wsgi
        1. latest sources are at https://github.com/GrahamDumpleton/mod_wsgi/releases
        1. `curl https://codeload.github.com/GrahamDumpleton/mod_wsgi/tar.gz/4.6.4 --output mod_wsgi.tgz`
        1. `tar -xvzf mod_wsgi.tgz; cd mod_wsgi-4.6.4; ./configure; make`
        1. exit (back to UNIX root shell), `cd /home/django/mod_wsgi-4.6.4; make install`

1.  configure httpd
    1.  edit /etc/httpd/conf/httpd.conf (as root)
```
WSGIScriptAlias / /home/django/django-lab/mvp/mvp/wsgi.py
WSGIPythonHome /home/django/venv
WSGIPythonPath /home/django/django-lab/mvp

<Directory /home/django/django-lab/mvp>
  <Files wsgi.py>
    Require all granted
  </Files>
</Directory>

Alias /static/ /home/django/django-lab/mvp/static/
<Directory /home/django/django-lab/mvp/static>
  Require all granted
</Directory>

LoadModule wsgi_module /usr/lib64/httpd/modules/mod_wsgi.so
```
    1. ensure file permissions are ok
        1. chmod 750 /home/django
        1. chgrp -R apache /home/django
    1. restart httpd
        1. `service httpd restart`
        1. ensure mod_wsgi is loaded
            1. `httpd -M | grep -i wsgi`
    
1.  Almost done!  Visit your EC2 instance w/a browser, 
python manage.py collectstatic
