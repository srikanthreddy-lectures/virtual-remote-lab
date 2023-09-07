output "ec_address" {
  value = "${aws_instance.web.public_ip}"
}
