[![Build Status](https://travis-ci.org/bertini36/serverless-email-sender.svg?branch=master)](https://travis-ci.org/bertini36/serverless-comments-engine)
[![Requirements Status](https://requires.io/github/bertini36/serverless-email-sender/requirements.svg?branch=master)](https://requires.io/github/bertini36/serverless-comments-engine/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/bertini36/serverless-email-sender/badge.svg?branch=master)](https://coveralls.io/github/bertini36/serverless-comments-engine?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<h3 align="center">
    bertini36/serverless-email-sender 📬
</h3>
<p align="center">
  <a href="#-environment-setup" target="_blank">
    Installation
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/serverless-email-sender/blob/master/serverless.yml" target="_blank">
    Serverless config
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/serverless-email-sender/blob/master/Makefile" target="_blank">
    Commands
  </a>
</p>
<p align="center">
A simple app to send emails deployed without cost using
<a href="https://www.serverless.com/" target="_blank">Serverless</a> framework and
<a href="https://aws.amazon.com/" target="_blank">AWS</a>.
</p>
<p align="center">
Powered by <a href="https://www.serverless.com/" target="_blank">#serverless</a> and
<a href="https://aws.amazon.com/" target="_blank">#aws</a>.
</p>

## ⚙️ Environment Setup

### 🐳 Required tools

1. [Install Docker and Docker Compose](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/bertini36/serverless-email-sender`
3. Move to the project folder: `serverless-email-sender`

## 🚀 Deploy

First set your AWS credentials
```bash
cp .env-sample .env
```

Ensure that your AWS user group has the required roles:
TODO

After this, to update your lambda functions
```bash
make deploy
```

<br />
<p align="center">&mdash; Built with :heart: from Mallorca &mdash;</p>
