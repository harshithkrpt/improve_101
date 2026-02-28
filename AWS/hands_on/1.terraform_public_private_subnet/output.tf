# Output the Public IP of the EC2 Instance in Public Subnet
output "public_instance_ip" {
    value = aws_instance.public_instance.public_ip
}

# Output the Private IP of the EC2 Instance in Private Subnet
output "private_instance_ip" {
    value = aws_instance.private_instance.private_ip
}

# Output the Elastic IP associated with the EC2 Instance in Public Subnet
output "public_instance_eip" {
    value = aws_eip.nat_eip.public_ip
}