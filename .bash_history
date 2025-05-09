yum update -y
yum install docker -y
systemctl start docker
systemctl enable  docker
docker --version
usermod -aG docker ec2-user
logout
