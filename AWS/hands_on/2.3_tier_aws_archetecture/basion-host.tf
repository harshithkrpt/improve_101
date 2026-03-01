module "public_bastion_sg" {
  source  = "terraform-aws-modules/security-group/aws"
  version = "5.3.1"
  name = "${var.vpc_name}-public-bastion-sg"
  description = "Security group for public bastion host for ssh port for everyone and all outbound traffic allowed"
  vpc_id = module.vpc.vpc_id
  
  ingress_rules = ["ssh-tcp"]
  ingress_cidr_blocks = ["0.0.0.0/0"]
  egress_rules = ["all-all"]

  tags = merge(
    var.common_tags,
    {
      Name = "${var.vpc_name}-public-bastion-sg"
    }
  )
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
  filter {
    name = "root-device-type"
    values = ["ebs"]
  }
  
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["amazon"]
}

module "public_bastion_host" {
  source  = "terraform-aws-modules/ec2-instance/aws"

  name = "${var.vpc_name}-public-bastion-host"
  ami = data.aws_ami.amazon_linux_2.id

  instance_type = var.instance_type
  key_name      = var.instance_keypair
  vpc_security_group_ids = [module.public_bastion_sg.security_group_id]

  subnet_id     = module.vpc.public_subnets[0]

  tags = merge(
    var.common_tags,
    {
      Name = "${var.vpc_name}-public-bastion-host"
    }
  )
}

# Associate Elastic IP with the public bastion host to ensure it has a static public IP address
resource "aws_eip" "public_bastion_host_eip" {
  instance = module.public_bastion_host.id
  

  tags = merge(
    var.common_tags,
    {
      Name = "${var.vpc_name}-public-bastion-host-eip"
    }
  )

  depends_on = [module.public_bastion_host, module.vpc]
}

resource null_resource "copy_ec2_keys" {
  depends_on = [module.public_bastion_host, aws_eip.public_bastion_host_eip]
  # Connection Block to copy the private key to the bastion host
  connection {
    type        = "ssh"
    host        = aws_eip.public_bastion_host_eip.public_ip
    user        = "ec2-user"
    private_key = file("./private_key/terraform_practice.pem")
  }

  # File provisioner to copy the private key to the bastion host
  provisioner "file" {
    source      = "./private_key/terraform_practice.pem"
    destination = "/tmp/terraform_practice.pem"
  }

  # Remote-exec provisioner to set permissions on the private key file
  provisioner "remote-exec"  {
    inline = [
      "sudo chmod 400 /tmp/terraform_practice.pem"
    ]
  }

  # Local-exec provisioner to print the public IP of the bastion host - Learning Point this in production is not needed as you would typically use a DNS name or have the IP address stored in a variable for later use, but it's useful for demonstration purposes to see the output directly in the console.
  provisioner "local-exec" {
    command = "echo 'Public IP of the bastion host: ${aws_eip.public_bastion_host_eip.public_ip}'"
  }
}