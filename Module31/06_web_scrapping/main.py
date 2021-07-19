import requests
import re

adress = 'http://www.columbia.edu/~fdc/sample.html'

data = requests.get(adress).text

pattern = r'<h3.+>(.*)</h3>'

result_list = re.findall(pattern, data)
print(result_list)
