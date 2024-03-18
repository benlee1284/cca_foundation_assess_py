import requests as requests

from src.regions.constants import Regions


def calculate_shipping(country, order_total):
    url = (
        "https://npovmrfcyzu2gu42pmqa7zce6a0zikbf.lambda-url.eu-west-2.on.aws/?country="
        + country
    )

    response = requests.get(url)
    response.raise_for_status()

    region = response.json()["region"]

    shipping = 0.0

    if region == Regions.UK.value:
        if order_total < 100.0:
            shipping = 4.99

    if region == Regions.EU.value:
        if order_total < 100:
            shipping = 8.99
        else:
            shipping = 4.99

    if region == Regions.OTHER.value:
        shipping = 9.99

    return shipping
