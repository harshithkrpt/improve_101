module "private_sg" {
    source  = "terraform-aws-modules/security-group/aws"
    version = "5.3.1"

    name        = "private-internal-sg"
    description = "Security group for private internal hosts"
    vpc_id      = module.vpc.vpc_id

    # Ingress rules
    ingress_rules = ["ssh-tcp", "http-80-tcp"]
    ingress_cidr_blocks = [module.vpc.vpc_cidr_block]
 
    # Egress rules
    egress_rules  = ["all-all"]


    # Tags
    tags = local.common_tags
}