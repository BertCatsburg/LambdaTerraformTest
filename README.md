# Testing Terraform/Lambda/Github integration

This small project contains a number of Lambda functions. 

The idea is that another project with Terraform files git-clones this Repo during the Apply phase in Terraform.

In the Terraform project we will try to check if a new version of the code is available on GitHub (this repo), and then continue the Apply.
Otherwise, don't update.

Yes, I know, I'm using an IaC tool like Terraform for CI/CD now and should not do that.

## Files

- lambda_code.py 

  this contains the Lambda's. Will be split up in the near future, each Lambda its own file.
- main.py

  this file is used to test the lambda's locally. The file has no purpose in the Terraform tests.
