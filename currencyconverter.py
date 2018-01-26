# Currency Converter
# Written by Justin White
# Released under the MIT License https://opensource.org/licenses/MIT

import json
import urllib.request

# Print welcome info
print("Currency Converter")
print("Currency information provided by the free, open source Fixer API. Type QUIT to quit.")

print('\n\n')

# Loop that allows more than one conversion without restarting program
while True:
    base_currency_amount = input('Enter amount to convert: ')

    base_currency = input('Enter currency to convert from (e.g. USD): ').upper()

    convert_currency = input('Enter currency to convert to: ').upper()

    # Cannot convert to the same currency
    if base_currency == convert_currency:
        print('!!! You cannot convert to the same currency! !!!')
        continue

    # Build URL based on input
    url = 'http://api.fixer.io/latest?base=' + base_currency

    # Use urllib to get the JSON info from the API
    with urllib.request.urlopen(url) as response:
        raw_json_data = response.read()

    # Converts the downloaded info into a usable JSON object
    json_data = json.loads(raw_json_data)

    conversion_rate = float(json_data['rates'][convert_currency])

    converted_amount = float(base_currency_amount) * conversion_rate

    print('{} {} = {} {}'.format(base_currency_amount, base_currency, converted_amount, convert_currency))

    # See if user wants to make another conversion
    choice = input('Convert another? [Y/n]: ')
    if choice.upper() == 'N':
        break
