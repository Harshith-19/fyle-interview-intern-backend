# Fyle Backend Challenge

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install

```
docker-compose build
```
### Reset DB

```
docker-compose run web bash reset.sh
```
### Start Server

```
docker-compose up
```
### Run Tests

```
docker-compose run web pytest -vvv -s tests/
```

### Get Coverage Report

```
docker-compose run web pytest --cov
```
