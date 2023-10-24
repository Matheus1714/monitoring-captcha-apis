# Hastings Monitoring Captcha API's

![Banner Project](.github/banner.png)

This project aims to be an API that monitors the funds of several captcha APIs.

## Table of Contents

## Introduction

It is very common that sometimes it is possible to forget how much captcha is spent per month, but this API aims to facilitate this problem.

## Features

- [X] Integration with Anti-Captcha
- [X] Integration with Two-Captcha
- [X] Integration with Cap-Solver 
- [ ] Email notification with founds for each captcha
- [ ] Email notification when a captcha API is close to running out of funds

## DEMO

The working API is available at: [DEMO](https://hastings-monitoring-captcha-apis.vercel.app/)

## Getting Started

### Prerequisites

- python3

### Configuration

Before starting the project, put your API keys in the `env.local` file. There is an example `.env.example` that can be followed as a reference to complete the configuration.

```shell
API_KEY_ANTI_CAPTCHA=...
API_KEY_CAP_SOLVER=...
API_KEY_TWO_CAPCHA=...
```

### Installation (Development)

First create a virtual environment using `virtualenv`:

```shell
pip install virtualev
```

Then create the virtual environment and make sure it is activated:

```shell
virtualenv venv
```

Then install the project dependencies:

```shell
pip install -r requirements.txt
```

The minimum dependencies are:

```txt
pytest
requests
python-dotenv
Flask
requests
requests-mock
apscheduler
```

### Usage

#### [Development]

For development it is necessary to uncomment the lines:

```py
# settings.py
from dotenv import dotenv_values

config = dotenv_values(".env.local")

API_KEY_ANTI_CAPTCHA = config.get('API_KEY_ANTI_CAPTCHA', '')
API_KEY_CAP_SOLVER = config.get('API_KEY_CAP_SOLVER', '')
API_KEY_TWO_CAPCHA = config.get('API_KEY_TWO_CAPCHA', '')
```

Now run the command to start:

```shell
python -m flask run --host=0.0.0.0
```

Access `http://localhost:5000`.

Now Enjoy!!

#### [Docker]

To run the application with Docker, use the commands:/

1. Create a image

```shell
docker build -t hastings-monitoring-captcha-api .
```

2. Run Image

```shell
docker run -d -p 5000:5000 hastings-monitoring-captcha-api
```

Access `http://localhost:5000`.

#### [Deploy]

For delpoy it is necessary to uncomment the lines:

```py
# settings.py
import os

API_KEY_ANTI_CAPTCHA = os.environ.get('API_KEY_ANTI_CAPTCHA', '')
API_KEY_CAP_SOLVER = os.environ.get('API_KEY_CAP_SOLVER', '')
API_KEY_TWO_CAPCHA = os.environ.get('API_KEY_TWO_CAPCHA', '')
```

On the deployment platform you choose, remember to configure the environment variables.

```shell
API_KEY_ANTI_CAPTCHA=...
API_KEY_CAP_SOLVER=...
API_KEY_TWO_CAPCHA=...
```

## License

This project is licensed under the [LICENSE](LICENSE) - see the LICENSE file for details.