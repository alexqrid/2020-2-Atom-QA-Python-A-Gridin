FROM centos:latest

RUN yum update -y
RUN yum install -y nginx

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]