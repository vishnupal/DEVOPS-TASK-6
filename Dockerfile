FROM centos:latest 
RUN yum install httpd -y
COPY * /var/www/html/
CMD /usr/sbin/httpd -DFOREGROUND && /bin/bash
