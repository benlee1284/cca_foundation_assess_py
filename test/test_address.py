from src.address import Address
from src.countries import Country


def test_instantiate_address():
    # This test is overkill, but it's here for demo purposes
    address = Address(
        house="1",
        street="High Street",
        city="Anytown",
        postcode="12345",
        country=Country.UNITED_KINGDOM,
    )
    assert address.house == "1"
    assert address.street == "High Street"
    assert address.city == "Anytown"
    assert address.postcode == "12345"
    assert address.country == Country.UNITED_KINGDOM
