module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my_terraform_vpc"
  cidr = "10.0.0.0/16"

  azs             = ["ap-south-1a", "ap-south-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  create_database_subnet_group = true
  create_database_subnet_route_table = true
  database_subnets = ["10.0.151.0/24", "10.0.152.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true


  enable_dns_hostnames = true
  enable_dns_support = true
  
  public_subnet_tags = {
    Terraform = "true"
  }

  private_subnet_tags = {
    Terraform = "true"
  }

  database_subnet_tags = {
    Terraform = "true"
  }

  tags = local.common_tags
}