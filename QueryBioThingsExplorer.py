import requests
import sys

class QueryBioThingsExplorer:

    def __init__(self):
        self.verbose = False
        self.API_BASE_URL = 'http://biothings.io/explorer/api/v2/directinput2output?input_prefix={input-prefix}&output_prefix={output-prefix}&input_value={input-value}'
        self.TIMEOUT_SEC = 120

    def send_query_get(self, input_prefix, output_prefix, input_value, verbose=False):
        url = self.API_BASE_URL.replace('{input-prefix}', input_prefix).replace('{output-prefix}', output_prefix).replace('{input-value}', input_value)
        try:
            res = requests.get(url,
                               timeout=self.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            if verbose:
                print(url, file=sys.stderr)
                print('Timeout in QueryBioThingsExplorer for URL: ' + url, file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            if verbose:
                print(url, file=sys.stderr)
                print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.json()