# ClouDDNSflare
A Docker DDNS/DynDNS (Dynamic DNS) alternative for your domains set up in Cloudflare. 
Access your home network from the outside with your own domain without worrying about dynamic IP!

## Usage
You just need to start a Docker container:

### Docker run
```bash
docker run -d \
--restart always \
-e PUBLIC_IP_PROVIDER=https://api.ipify.org \
-e REFRESH_MINUTES=5 \
-e CF_API_URL=https://api.cloudflare.com/client/v4 \
-e CF_API_EMAIL=youremail@gmail.com \
-e CF_API_KEY=cf_global_api_key \
-e CF_ZONE=yourdomain.com \
-e CF_RECORD=subdomain.yourdomain.com \
m4rc0sx/clouddnsflare:latest
```

### Docker compose
```yml
version: '3.8'

services:
  clouddnsflare:
    image: m4rc0sx/clouddnsflare:latest
    restart: always
    environment:
      PUBLIC_IP_PROVIDER: https://api.ipify.org
      REFRESH_MINUTES: 5
      CF_API_URL: https://api.cloudflare.com/client/v4
      CF_API_EMAIL: youremail@gmail.com
      CF_API_KEY: cf_global_api_key
      CF_ZONE: yourdomain.com
      CF_RECORD: subdomain.yourdomain.com

```
```bash
docker compose up -d
```

## Env variables
| Option            | Description                                      | Type      | Default             |
|-------------------|--------------------------------------------------|-----------|---------------------|
| `PUBLIC_IP_PROVIDER` | The URL of the public IP provider            | String| `https://api.ipify.org`|
| `REFRESH_MINUTES` | The interval in minutes to refresh the IP address. **Be careful with CF rate limits!** | Integer| `5`                 |
| `CF_API_URL`     | The URL of the Cloudflare API                    | String| `https://api.cloudflare.com/client/v4`|
| `CF_API_EMAIL`   | Your Cloudflare account email                    | String|     `""`                |
| `CF_API_KEY`     | Your Cloudflare API key                          | String| `""` |
| `CF_ZONE`        | Your Cloudflare Zone name                          | String| `""`    |
| `CF_RECORD`      | The DNS record you want to update                | String| `""`|



