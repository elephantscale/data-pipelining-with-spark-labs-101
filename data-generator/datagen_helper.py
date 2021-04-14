import random
import pandas as pd
import string
from datetime import datetime
import dateutil.parser
import uuid

# here is the reference : https://en.wikipedia.org/wiki/ISO_8583

# digits = '0123456789'
digits = string.digits
digits10 = digits * 10

## Credit card numbers are 16 digits
## Visa cards start with 4
def generate_credit_card_number():
    s1 = ''.join(random.sample(digits10, 15))
    s3 = f'4{s1}'
    return s3


# A charge amount between 1 - 1000
def generate_amount():
    return random.randint(1,10000) / 100

## 1 - 99
def generate_merchant_type():
    r =  random.randint(1,9999)
    return '{:04d}'.format(r)

def generate_merchant_id():
    r =  random.randint (1, 150)
    if r <= 100:
        return r
    else:
        return 0

merchant_name_1 = ['Super', 'Awesome', 'Best', 'Sunny', 'First', 'Summer Winds', 'Four Seasons', 'Sun Shine', 'Star']
merchant_name_2 = ['Dry cleaners', 'Restaurant', 'Auto', 'Flowers', 'Bakery', 'Toys', 'Nursery', 'Hardware', 'Liquors', 'Donuts']
def generate_merchant_name():
    return f'{random.choice(merchant_name_1)} {random.choice(merchant_name_2)}'


streets = ['Main st', 'Broadway', 'Hillview St', 'Market St', 'Beach rd', 'Alameda ave']
cities = ('San Jose', 'San Francisco', 'Redwood City', 'Foster City', 'Burlingame', 'San Mateo')
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
countries = ['USA']

def generate_address():
    return f'{random.randint(1,1000)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(states)}, {random.choice(countries)}'


def generate_merchant_address():
    return f'{generate_merchant_name()}, {generate_address()}'

## returns timestamp_ms
start_timestamp = datetime(2015, 1, 1)
## convert to milliseconds
start_timestamp_ms = int (start_timestamp.timestamp() * 1000)

end_timestamp = datetime(2020, 12, 31)
end_timestamp_ms = int (end_timestamp.timestamp() * 1000)

def generate_timestamp_ms():
    return random.randint (start_timestamp_ms, end_timestamp_ms)

def convert_timestamp_from_ms_to_iso(ts_ms):
    return datetime.fromtimestamp(ts_ms/1000.0).isoformat(sep=' ', timespec='milliseconds')

# def generate_request_reponse():
#     timestamp_request = generate_timestamp_ms()
    
#     request = {}
#     request['id'] = uuid.uuid4()
#     request['timestamp'] = convert_timestamp_from_ms_to_iso(timestamp_request)
#     request['mti'] = '0100'
#     request['card_number'] = generate_credit_card_number()
#     request['amount_customer'] = generate_amount()
#     request['amount_merchant'] = round (request['amount_customer'] * 0.97, 2)
    
#     response = {}
#     response['id'] = request['id']
#     timestamp_response = timestamp_request + random.randint(200,2000)
#     response['timestamp'] = convert_timestamp_from_ms_to_iso(timestamp_response)
#     response['mti'] = '0110'
#     return (request , response)
# ## --- end : def generate_request_reponse():


def generate_request():
    request = {}
    request['id'] = uuid.uuid4()
    request['timestamp'] = convert_timestamp_from_ms_to_iso(generate_timestamp_ms())
    request['mti'] = '0100'
    request['card_number'] = generate_credit_card_number()
    request['amount_customer'] = generate_amount()
    request['merchant_type'] = generate_merchant_type()
    request['merchant_id'] = generate_merchant_id()
    request ['merchant_address'] = generate_merchant_address()
    request['ref_id'] = ""
    return request
## --- end : def generate_request_reponse():


## response codes are generated from request
response_codes = (
                    '00',   # approved
                    '03',   # invalid_merchant
                    '06',   # error 
                    '08',   # Honour with identification
                    '13',   # Invalid amount
                    '14',   # Invalid card number
                    '33',   # Expired card
                    )
response_code_weights = (80, 2, 1, 10, 4, 2, 1)
def generate_response(request):
    response = {}
    response['ref_id'] = request['id']
    response['id'] = uuid.uuid4()
    request_timestamp = dateutil.parser.parse(request['timestamp'])
    request_timestamp_ms = int (request_timestamp.timestamp() * 1000)
    # add a few hundred millisecond delay
    response_timestamp_ms = request_timestamp_ms + random.randint (300, 3000)
    response['timestamp'] = convert_timestamp_from_ms_to_iso (response_timestamp_ms)
    response['mti'] = '0110'
    response['card_number'] = request['card_number']
    response['amount_customer'] = request['amount_customer']
    response['amount_merchant'] = round (request['amount_customer'] * 0.97, 2)
    response['merchant_type'] = request['merchant_type']
    response['merchant_id'] = request['merchant_id']
    response['merchant_address'] = request['merchant_address']
    
    response ['response_code'] = random.choices(population = response_codes, weights=response_code_weights, k=1)[0]
    return response
## ---- end : def generate_response(request):


def generate_pd_df(rows=10):
    df_pd = pd.DataFrame()
    for i in range (0, rows//2):
        request = generate_request()
        request_df = pd.DataFrame.from_dict([request])
        response = generate_response (request)
        response_df = pd.DataFrame.from_dict([response])
        df_pd = pd.concat( [df_pd, request_df, response_df], join='outer', copy=False, ignore_index=True)

    # make UUIDs are Strings for easier conversion to Spark
    df_pd['id'] = df_pd['id'].astype('string') 
    df_pd['ref_id'] = df_pd['ref_id'].astype('string')
    return df_pd
## ---- end: def generate_pd_df(rows=10):

