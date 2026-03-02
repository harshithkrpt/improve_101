resource "null_resource" "remote_exec" {
  depends_on = [module.ec2_public]

  connection {
    type        = "ssh"
    host        = module.ec2_public.public_ip
    user        = "ec2-user"        
    private_key = file("./private-keys/terraform_practice.pem")
    timeout     = "2m"
  }

  provisioner "file" {
    source      = "./private-keys/terraform_practice.pem"
    destination = "/tmp/terraform_practice.pem"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo chmod 400 /tmp/terraform_practice.pem",
    ]
  }

  provisioner "local-exec" {
    command = "echo VPC created on $(date) >> vpc_creation_log.txt"
    working_dir = "local-exec-output-files/"
  }

  # provisioner "local-exec" {
  #   command = "echo VPC Deleted on $(date) >> vpc_deletion_log.txt"
  #   when    = destroy
  #   working_dir = "local-exec-output-files/"
  # }
}