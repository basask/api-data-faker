# Api Data Faker

API Data Faker is an fake data generator with a rest API embeded.

It was develop to test data pipelines through REST APIS.


# Usage

``` bash
# Clone the repository
git clone git@github.com:basask/api-data-faker.git

# Change into the app directory
cd api-data-faker

# Install dependencies. Better use a virtual enviroment (https://docs.python.org/3/library/venv.html)
pip install -r requirements.txt

# Running the services
python main.py service_c service_b service_a
```

You'll problably need to make some changes in the factories to reflect your data needs. This can be changed in the factories.py file.

Also, additional services can be added in the main.py through variable SERVICE_MAP


# Docker

Running with docker
``` bash
# Clone the repository
git clone git@github.com:basask/api-data-faker.git

# Change into the app directory
cd api-data-faker

# Building docker image
docker build -t api-data-faker .

# Running docker image
docker run -p 8881:8881 -p 8882:8882 -p 8883:8883 api-data-faker
```

# Testing

``` bash
curl http://localhost:8881/07385694387
curl http://localhost:8882/07385694387
curl http://localhost:8883/07385694387
```
