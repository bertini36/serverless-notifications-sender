[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<h3 align="center">
    bertini36/serverless-notifications-sender 📬
</h3>
<p align="center">
  <a href="#-environment-setup" target="_blank">
    Installation
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/serverless-notifications-sender/blob/master/serverless.yml" target="_blank">
    Serverless config
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/serverless-notifications-sender/blob/master/Makefile" target="_blank">
    Commands
  </a>
</p>
<p align="center">
A simple app to send notification emails to yourself deployed without cost using
<a href="https://www.serverless.com/" target="_blank">Serverless</a> framework and
<a href="https://aws.amazon.com/" target="_blank">AWS</a>
</p>
<p align="center">
Powered by <a href="https://www.serverless.com/" target="_blank">#serverless</a> and
<a href="https://aws.amazon.com/" target="_blank">#aws</a>
</p>

## ⚙️ Environment Setup

### 🐳 Required tools

1. [Install Docker and Docker Compose](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/bertini36/serverless-notifications-sender`
3. Move to the project folder: `serverless-notifications-sender`

## 🚀 Deploy

First set your AWS credentials and your sender and recipient email addresses.
```bash
cp .env-sample .env
```
Keep in mind that both email addresses have to be verified at your AWS SES console.

To deploy your lambda functions
```bash
make deploy
```
When deploy is finished you will see the app endpoint.

### 👩‍💻 Send a notification
```python
import json
import requests

response = requests.post(
    '<APP_ENDPOINT>/send/email',
    json.dumps({'subject': 'Ouh', 'message': 'mama'}),
    headers={'Content-Type': 'application/json'}
)
```

<br />
<p align="center">&mdash; Built with :heart: from Mallorca &mdash;</p>
