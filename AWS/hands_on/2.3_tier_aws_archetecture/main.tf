data "aws_availability_zones" "available" {
  exclude_names = var.exclude_azs
}


module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 6.6.0"

  name = var.vpc_name
  cidr = var.vpc_cidr

  azs             = data.aws_availability_zones.available.names
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  database_subnets                    = var.database_subnets
  create_database_subnet_group        = true
  create_database_subnet_route_table  = true

  enable_nat_gateway = var.enable_nat_gateway
  single_nat_gateway = var.single_nat_gateway

  enable_dns_hostnames = true
  enable_dns_support   = true

  public_subnet_tags = {
    Name = "${var.vpc_name}-public"
  }

  private_subnet_tags = {
    Name = "${var.vpc_name}-private"
  }

  database_subnet_tags = {
    Name = "${var.vpc_name}-database"
  }

  tags = var.common_tags

  vpc_tags = {
    Name = var.vpc_name
  }
}