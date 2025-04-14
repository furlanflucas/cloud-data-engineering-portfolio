provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "flucas-devops-demo-bucket"
  versioning {
    enabled = true
  }
}
