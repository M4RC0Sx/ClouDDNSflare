import logging

import requests


class CloudflareAPI:
    def __init__(
        self,
        email: str,
        key: str,
        zone: str,
        record: str,
        cf_api: str,
        public_ip_provider: str,
    ) -> None:
        self.email = email
        self.key = key
        self.zone = zone
        self.record = record
        self.cf_api = cf_api

        self.public_ip_provider = public_ip_provider

        self.zone_id: str | None = None
        self.record_id: str | None = None

    def __get_cf_headers(self) -> dict[str, str]:
        return {
            "X-Auth-Email": self.email,
            "X-Auth-Key": self.key,
            "Content-Type": "application/json",
        }

    def __get_public_ip(self) -> str:
        return requests.get(self.public_ip_provider).text

    def __get_zone_id(self) -> str:
        if self.zone_id:
            return self.zone_id

        url = f"{self.cf_api}/zones?name={self.zone}"
        headers = self.__get_cf_headers()
        response = requests.get(url, headers=headers)
        return str(response.json()["result"][0]["id"])

    def __get_record_id(self, zone_id: str) -> str:
        if self.record_id:
            return self.record_id

        url = f"{self.cf_api}/zones/{zone_id}/dns_records"
        headers = self.__get_cf_headers()
        params = {"name": self.record, "type": "A"}
        response = requests.get(url, headers=headers, params=params)
        return str(response.json()["result"][0]["id"])

    def update_dns_record(self) -> None:
        zone_id = None
        record_id = None
        public_ip = None

        try:
            zone_id = self.__get_zone_id()
        except Exception as e:
            logging.error(f"Error getting zone ID: {e}")
            raise e
        self.zone_id = zone_id
        try:
            record_id = self.__get_record_id(zone_id)
        except Exception as e:
            logging.error(f"Error getting record ID: {e}")
            raise e
        self.record_id = record_id
        try:
            public_ip = self.__get_public_ip()
        except Exception as e:
            logging.error(f"Error getting public IP: {e}")
            raise e

        url = f"{self.cf_api}/zones/{zone_id}/dns_records/{record_id}"
        headers = self.__get_cf_headers()
        data = {
            "type": "A",
            "name": self.record,
            "content": public_ip,
            "proxied": False,
        }
        requests.put(url, headers=headers, json=data)
        logging.info(f"DNS record updated to {public_ip}")
