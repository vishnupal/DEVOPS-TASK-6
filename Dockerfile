FROM centos:latest 
RUN yum install httpd -y
COPY /storage/ /var/www/html/
CMD /usr/sbin/httpd -DFOREGROUND && /dev/bash
