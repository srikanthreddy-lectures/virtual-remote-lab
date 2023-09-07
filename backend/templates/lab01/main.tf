# Specify the provider and access details
provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "${var.aws_region}"
}


# Our default security group to access
# the instances over SSH and HTTP
resource "aws_security_group" "default" {
    name = "terraform_example"
    description = "Used in the terraform"

    # SSH access from anywhere
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    # ALL access from anywhere
    ingress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks      = ["0.0.0.0/0"] 
        ipv6_cidr_blocks = ["::/0"]
    }

    # outbound internet access
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "web" {
  # The connection block tells our provisioner how to
  # communicate with the resource (instance)
  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("./test.pem")
    host        = self.public_ip

  }

  instance_type = "t2.medium"

  # Lookup the correct AMI based on the region
  # we specified
  ami = "${lookup(var.aws_amis, var.aws_region)}"

  # The name of our SSH keypair you've created and downloaded
  # from the AWS console.
  #
  # https://console.aws.amazon.com/ec2/v2/home?region=us-west-2#KeyPairs:
  #
  key_name = "${var.key_name}"

  # Our Security group to allow HTTP and SSH access
  security_groups = ["${aws_security_group.default.name}"]

  tags = {
    Name ="Lab01"
    Environment = "lab01"
    OS = "UBUNTU"
    Managed = "IAC"
  }

  # root disk
  root_block_device {
    volume_size           = "20"
    volume_type           = "gp2"
    encrypted             = false
    delete_on_termination = true
  }

  # We run a remote provisioner on the instance after creating it.
  provisioner "file" {
      source = "./lab.sh"
      destination = "/tmp/"
  } 
provisioner "remote-exec" {
   inline = [
        "sh /tmp/lab.sh",
    ]
  }
}