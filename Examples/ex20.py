import requests

base_url = 'http://kelutral.com/old_ci/randomdata/contacts/'

# philips_proxies = dict(http='http://165.225.96.34:9480')

id = input('Enter id: ')

# resp = requests.get(base_url + id, proxies = philips_proxies)
resp = requests.get(base_url + id)
resp_json = resp.json()
print(resp_json)

print('-'*80)

my_info = dict(first_name='Vinod', last_name='Kumar', gender='Male',
	email='vinod@vinod.co', phone='9731424784')

# requests.post(base_url, data=my_info, proxies=philips_proxies)
resp = requests.post(base_url, json=my_info)
print(resp.json())