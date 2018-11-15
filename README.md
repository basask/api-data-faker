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
