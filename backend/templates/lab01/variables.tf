variable "key_name" {
    description = "test"
    default = "test"
}

variable "key_path" {
    description = "./test.pem123"
    default = "./test.pem123"
}

variable "access_key" {default = "<>"}
variable "secret_key" {default ="<>"}

variable "aws_region" {
    description = "AWS region to launch servers."
    default = "us-east-1"
}

# Ubuntu Server 22.04 LTS (x64)
variable "aws_amis" {
    default = {
        us-east-1 = "ami-0c7bb2de87d4a1637"
    }
}

