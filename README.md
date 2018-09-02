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

I will created an account "django" to hold the django application.  
httpd (apache) will use uwsgi as a bridge to django.  "django" (the 
UNIX account) will need to be a member of the apache (UNIX) group.

## EC2 (deployment environment)

1.  Start an EC2 instance.  Original MVP development was on a M4.small 
instance using a LINUX2 AMI. 

1.  Install these packages
    1. `yum -y install python3`
    1. `yum -y install python3-devel`
    1. `yum -y install httpd-devel`
    1. `yum -y groupinstall 'Development Tools'`
    1. `yum -y install postgresql`
    1. `yum -y install postgresql-server`

1.  Create database
    1. postgres/genesis
    1. service postgresql initdb
    1. edit /var/lib/pgsql/data/pg_hba.conf and postgresql.conf

service postgresql start

su - postgres
psql -U postgres
alter user postgres with password 'flyaway';

python manage.py createsuperuser
gsc/bogus

1.  Create a LINUX user account 'django' and add it the 'apache' group
    1. useradd -m django
    1. usermod -a -G apache django
    1. chown -R django:apache /var/www
    1. sudo chmod 2775 /var/www
    
1.  Create a python virtualenv for python3

1.  As the user 'django', check out 'django-lab' from github


pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
Successfully installed uWSGI-2.0.17.1

find /var/www -type d -exec sudo chmod 2775 {} \;

/usr/lib64/httpd/modules/mod_wsgi.so

[root@ip-172-31-13-21 home]# chmod 750 django
[root@ip-172-31-13-21 home]# chgrp -R apache django

python manage.py collectstatic
