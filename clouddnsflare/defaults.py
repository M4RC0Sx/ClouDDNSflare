from enum import Enum


class DefaultConfig(Enum):
    # Public IP service provider
    PUBLIC_IP_PROVIDER = "https://api.ipify.org"
    # Refresh minutes
    REFRESH_MINUTES = 5
    # Cloudflare API URL
    CF_API_URL = "https://api.cloudflare.com/client/v4"
    # Cloudflare API email
    CF_API_EMAIL = ""
    # Cloudflare API key
    CF_API_KEY = ""
    # Cloudflare zone
    CF_ZONE = ""
    # Cloudflare record
    CF_RECORD = ""
