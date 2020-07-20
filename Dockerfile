FROM centos:latestRUN yum install httpd -y
COPY *.html /var/www/html/
CMD /usr/sbin/httpd -DFOREGROUND && /dev/bash
