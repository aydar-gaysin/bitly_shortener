# Bitly URLs shortener and clicks monitor

Console utility URL with Bitly service or to get number of clicks on your shortened link.
Interacts with Bitly API with request module. Written on Python3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need:
* Python 3.x installed.
* [Bitly GENERIC ACCESS TOKEN](https://bitly.com/a/oauth_apps)

### Installing

Install all required packages with PIP:

```
pip install -r requirements.txt
```
Create .env file and put in your [Bitly GENERIC ACCESS TOKEN](https://bitly.com/a/oauth_apps)
```
BITLY_TOKEN=
``` 
## How to use

Utility used from console.
Just start main.py script giving your URL or bitlink as argument:

```
$ python3 main.py https://jenyay.net/Programming/Argparse
Битлинк:  https://bit.ly/3hsMLFs

$ python3 main.py https://bit.ly/3hsMLFs
Кликов:  0

```
## Acknowledgments
As this code was written as part of online developer training project
I express my appreciation and gratitude to [devman.org](https://bit.ly/36JNmPc) team. 