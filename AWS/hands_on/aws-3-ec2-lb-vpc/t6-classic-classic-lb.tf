
# Security group for Public Load Balancer
module "load_balancer_sg" {
    source  = "terraform-aws-modules/security-group/aws"
    version = "5.3.1"

    name        = "load-balancer-sg"
    description = "Security group for load balancer"
    vpc_id      = module.vpc.vpc_id

    # Ingress rules
    ingress_rules = ["http-80-tcp"]
    ingress_cidr_blocks = ["0.0.0.0/0"]
 
    # Egress rules
    egress_rules  = ["all-all"]


    # Tags
    tags = local.common_tags
}


module "elb" {
  source  = "terraform-aws-modules/elb/aws"

  name = "my-classic-elb-http"

  subnets         = module.vpc.public_subnets
  security_groups = [module.load_balancer_sg.security_group_id]
  internal        = false

  listener = [
    {
      instance_port     = 80
      instance_protocol = "HTTP"
      lb_port           = 80
      lb_protocol       = "HTTP"
    },
    {
      instance_port     = 81
      instance_protocol = "HTTP"
      lb_port           = 81
      lb_protocol       = "HTTP"
      # ssl_certificate_id = "arn:aws:acm:eu-west-1:235367859451:certificate/6c270328-2cd5-4b2d-8dfd-ae8d0004ad31"
    },
  ]

  health_check = {
    target              = "HTTP:80/"
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 5
  }

  access_logs = {
    bucket = "my-access-logs-bucket"
  }

  // ELB attachments - attach EC2 instances to the ELB (Target group in case of ALB)
  number_of_instances = length(module.ec2_private)
  instances           = [for instance in module.ec2_private : instance.id]
  tags = local.common_tags
}