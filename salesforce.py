from simple_salesforce import Salesforce
from decouple import config

sf = Salesforce(
    client_id=config('CLIENT_ID'),
    domain='test',
    consumer_key=config('CONSUMER_KEY'),
    username=config('USERNAME'),
    password=config('PASSWORD'),
    privatekey_file=config('PRIVATEKEY_FILE')
)


def query():
    results = sf.query_all("SELECT Id, Name FROM Account LIMIT 5")

    print(results)


if __name__ == "__main__":
    query()
