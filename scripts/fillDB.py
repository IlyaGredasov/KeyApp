import requests
from faker import Faker

faker = Faker()

for i in range(30):
    body = {
        "login": faker.user_name(),
        "password": faker.password(),
        "domain": faker.domain_name()
    }
    r = requests.post(url=f'http://10.55.0.1:8000/add_data',
                      json=body)
