# Create VPC 
resource "aws_vpc" "main" {
  cidr_block = "10.100.0.0/16"
  
  tags = {
    Name = "terraform-vpc"
  }
}

# Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "terraform-igw"
  }
}

# Create Public Subnet
resource "aws_subnet" "public" {
    vpc_id            = aws_vpc.main.id
    cidr_block        = "10.100.0.0/24"
    availability_zone = "ap-south-1a"
    # To assign public IP to EC2 instance in public subnet, we need to set this parameter to true
    map_public_ip_on_launch = true


    tags = {
      Name = "terraform-public-subnet"
    }
}

# Create Private Subnet
resource "aws_subnet" "private" {
    vpc_id            = aws_vpc.main.id
    cidr_block        = "10.100.1.0/24"
    availability_zone = "ap-south-1b"

    tags = {
      Name = "terraform-private-subnet"
    }
}


# Create Route Table for Public Subnet
resource "aws_route_table" "public" {
    vpc_id = aws_vpc.main.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.gw.id
    }

    tags = {
      Name = "terraform-public-rt"
    }
}

# Associate Public Subnet with Route Table
resource "aws_route_table_association" "public" {
    subnet_id      = aws_subnet.public.id
    route_table_id = aws_route_table.public.id
}




# Create NAT Gateway in Public Subnet
resource "aws_eip" "nat_eip" {
  domain = "vpc"

  tags = {
    Name = "terraform-nat-eip"
  }
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "terraform-nat-gateway"
  }
}

# Create Route Table for Private Subnet
resource "aws_route_table" "private" {
    vpc_id = aws_vpc.main.id

    route {
        cidr_block     = "0.0.0.0/0"
        nat_gateway_id = aws_nat_gateway.nat.id
    }

    tags = {
      Name = "terraform-private-rt"
    }
}

# Associate Private Subnet with Route Table
resource "aws_route_table_association" "private" {
    subnet_id      = aws_subnet.private.id
    route_table_id = aws_route_table.private.id
}


# Create Security Group for Public Subnet -> Only Allow SSH From anywhere
resource "aws_security_group" "public_sg" {
    name        = "terraform-public-sg"
    description = "Allow SSH from my IP"
    vpc_id      = aws_vpc.main.id


    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
      Name = "terraform-public-sg"
    }
}

# Create Security Group for Private Subnet -> Only Allow SSH From Public Subnet
resource "aws_security_group" "private_sg" {
    name        = "terraform-private-sg"
    description = "Allow SSH from public subnet"
    vpc_id      = aws_vpc.main.id

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = [aws_subnet.public.cidr_block]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
      Name = "terraform-private-sg"
    }
}

# Get the latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]


  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*"]
  }
}

# Create Key Pair to SSH into EC2 Instances
resource "aws_key_pair" "main" {
  key_name   = "terraform-main-key"
  public_key = file("${path.module}/terraform-key.pub")
}


# Create EC2 Instance in Public Subnet
resource "aws_instance" "public_instance" {
    ami           = data.aws_ami.amazon_linux.id
    instance_type = "t3.micro"

    subnet_id              = aws_subnet.public.id
    vpc_security_group_ids = [aws_security_group.public_sg.id]
    key_name               = aws_key_pair.main.key_name

    tags = {
      Name = "terraform-public-instance"
    }
}


# Create EC2 Instance in Private Subnet
resource "aws_instance" "private_instance" {
    ami           = data.aws_ami.amazon_linux.id
    instance_type = "t3.micro"

    subnet_id              = aws_subnet.private.id
    vpc_security_group_ids = [aws_security_group.private_sg.id]
    key_name               = aws_key_pair.main.key_name

    tags = {
      Name = "terraform-private-instance"
    }
}