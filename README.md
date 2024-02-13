# Coding challenges

This project has purpose of define different kind of PoC, testing concepts and searching ways to solve any requirement.

## Table of Contents

- [Token_bucket_rate_limit_v1](#Token_bucket_rate_limit_v1)
- [Backlog](#Backlog)

## Token_bucket_rate_limit_v1

This project test a basic Token bucket rate limit, which in this V1 only allows manual validation (F5) but apply rate limit in endpoint http://127.0.0.1:5000/api/limited 

## Backlog

- Improvement session managament to allow performance test with postman https://blog.postman.com/postman-api-performance-testing/

```bash
# Clone the repository
git clone https://github.com/joemacias/coding_challenges.git

# Change into the Token bucket rate limit v1 project directory
cd flask_basic_api

# Install dependencies
pip install flask

# Run project
python run.py