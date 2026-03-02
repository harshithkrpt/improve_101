module "public_bastion_sg" {
    source  = "terraform-aws-modules/security-group/aws"
    version = "5.3.1"

    name        = "public-bastion-sg"
    description = "Security group for bastion host, allowing SSH access from anywhere , egress is open to all"
    vpc_id      = module.vpc.vpc_id

    # Ingress rules
    ingress_rules = ["ssh-tcp"]
    ingress_cidr_blocks = ["0.0.0.0/0"]

    # Egress rules
    egress_rules  = ["all-all"]


    # Tags
    tags = local.common_tags
}