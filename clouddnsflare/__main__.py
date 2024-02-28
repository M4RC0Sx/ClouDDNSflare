from os import getenv
import sys
import logging
from time import sleep


from clouddnsflare.defaults import DefaultConfig
from clouddnsflare.cloudflare_api import CloudflareAPI


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logging.getLogger().addHandler(logging.StreamHandler())


PUBLIC_IP_PROVIDER = getenv(
    "PUBLIC_IP_PROVIDER", DefaultConfig.PUBLIC_IP_PROVIDER.value
)
REFRESH_MINUTES = int(getenv("REFRESH_MINUTES", DefaultConfig.REFRESH_MINUTES.value))
CF_API_URL = getenv("CF_API_URL", DefaultConfig.CF_API_URL.value)
CF_API_EMAIL = getenv("CF_API_EMAIL", DefaultConfig.CF_API_EMAIL.value)
CF_API_KEY = getenv("CF_API_KEY", DefaultConfig.CF_API_KEY.value)
CF_ZONE = getenv("CF_ZONE", DefaultConfig.CF_ZONE.value)
CF_RECORD = getenv("CF_RECORD", DefaultConfig.CF_RECORD.value)


def main() -> None:
    logging.info("ClouDDNSflare by M4RC0Sx (https://github.com/M4RC0Sx) is starting...")
    logging.info(f"Public IP provider: {PUBLIC_IP_PROVIDER}")
    logging.info(f"Refresh minutes: {REFRESH_MINUTES}")
    logging.info(f"Cloudflare zone: {CF_ZONE}")
    logging.info(f"Cloudflare record: {CF_RECORD}")

    cf_api = CloudflareAPI(
        email=CF_API_EMAIL,
        key=CF_API_KEY,
        zone=CF_ZONE,
        record=CF_RECORD,
        cf_api=CF_API_URL,
        public_ip_provider=PUBLIC_IP_PROVIDER,
    )

    while True:
        logging.info("Refreshing public IP...")

        try:
            cf_api.update_dns_record()
        except Exception as e:
            logging.error(f"There was an error updating DNS record: {e}. Exiting...")
            sys.exit(1)

        logging.info(f"Waiting {REFRESH_MINUTES} minutes before next refresh...")
        sleep(REFRESH_MINUTES * 60)


if __name__ == "__main__":
    main()
