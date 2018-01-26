import json
import urllib.request

class CurrencyConverter:
    def convert(amount_to_convert, convert_from, convert_to):

        # Build URL
        url = 'http://api.fixer.io/latest?base=' + convert_from

        # Use urllib to get the JSON info from the API
        with urllib.request.urlopen(url) as response:
            raw_json_data = response.read()

        # Converts the downloaded info into a usable JSON object
        json_data = json.loads(raw_json_data)

        # Fetch the conversion rate from JSON
        conversion_rate = float(json_data['rates'][convert_to])

        # Calculate converted amount
        converted_amount = float(amount_to_convert) * conversion_rate

        return converted_amount
