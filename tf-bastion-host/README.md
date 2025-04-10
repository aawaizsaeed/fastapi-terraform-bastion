
---

## `bastion-host/README.md` (Terraform Bastion EC2)

# Terraform Bastion Host on AWS

This Terraform configuration provisions a secure EC2 instance to be used as a **bastion host** inside an existing VPC with public subnets.

## Features

- EC2 instance in public subnet
- Security group with restricted SSH access
- Public IP for external access
- Variables for full flexibility
- Safe by default with `prevent_destroy` lifecycle rule

---


