import requests

try:
    response = requests.get('https://detik.com')
    if response.status_code == 200:
        print(f'Success! response = {response.status_code}')
        print(f'response {response.text}')
    else:
        print('There is a requests error')
except Exception as e:
    print(f'There is an error! {e}')
print('Program ended')
