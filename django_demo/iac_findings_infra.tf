resource "aws_db_instance" "app_db" {
  identifier        = "app-db"
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  storage_encrypted = false
  publicly_accessible = true
  password          = "hardcoded_password_123"
}

resource "aws_security_group" "open_sg" {
  name = "open-sg"
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
