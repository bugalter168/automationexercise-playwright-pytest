import random
import time
from dataclasses import dataclass

from faker import Faker

from utils.constants import COUNTRIES

fake = Faker()


@dataclass
class UserData:
    name: str
    email: str
    password: str
    title: str
    day: str
    month: str
    year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str


def unique_email(prefix: str = "qauser") -> str:
    return f"{prefix}.{int(time.time() * 1000)}.{random.randint(1000, 9999)}@example.com"


def generate_user() -> UserData:
    first_name = fake.first_name()
    last_name = fake.last_name()
    return UserData(
        name=f"{first_name} {last_name}",
        email=unique_email(),
        password=fake.password(length=12),
        title=random.choice(["Mr", "Mrs"]),
        day=str(random.randint(1, 28)),
        month=str(random.randint(1, 12)),
        year=str(random.randint(1970, 2000)),
        first_name=first_name,
        last_name=last_name,
        company=fake.company(),
        address1=fake.street_address(),
        address2=fake.secondary_address(),
        country=random.choice(COUNTRIES),
        state=fake.state(),
        city=fake.city(),
        zipcode=fake.postcode(),
        mobile_number=fake.msisdn()[:10],
    )
