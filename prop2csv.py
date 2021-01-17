# Aliens E2 Tools: prop2csv
# a Python script to export the properties of a given profile to a csv file
#
# Copyright (c) Michele Fabbri - fabbri.michele@gmail.com
# Released under the terms of the GNU GPL v3 License: https://www.gnu.org/licenses/gpl-3.0.en.html
#
# This software is provided ​“AS IS”. Michele Fabbri makes no other warranties, express or implied, and hereby disclaims all implied warranties,
# including any warranty of merchantability and warranty of fitness for a particular purpose.
#  
import requests
import json
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Alien\'s E2 Tools: Properties to CSV')
parser.add_argument('-i', '--id', required=True, dest='id', metavar='<user_id>', help='Specify user id, in the profile page, the string after \"https://app.earth2.io/#profile/\"')
parser.add_argument('-n', '--n', required=True, dest='n', metavar='<properties_count>', help='Specify a maximum number of properties to query')
parser.add_argument('-o', '--out', required=True, dest='out', metavar='<output_file>', help='Specify the output filename (eg: properties.csv)')
args = parser.parse_args()

e2id = args.id
e2n = args.n
e2out = args.out

query__properties = """query {
    getUserLandfields(userId: \"""" + e2id + """\", page: 1, items: """ + e2n + """) {
        count,
        landfields {
            id, forSale, description, location, center, price, country, tileCount, currentValue, tradingValue
        }
    }
}"""

url = 'https://app.earth2.io/graphql'
r = requests.post(url, json={'query': query__properties})
print('HTTP response: ' + str(r.status_code))
json_data = json.loads(r.text)
df_data = json_data['data']['getUserLandfields']['landfields']
df = pd.DataFrame(df_data)
df.head()
df[['longitude','latitude']] = df.center.str.split(expand=True) 
df.head()
df.to_csv(e2out, sep=',', quotechar="\"", encoding='utf-8')

print('Done.')
print('')
print('This tool has been kindly provided to you by a more evolved alien life form.')
print('Find me at the ALIEN GIGA-STRUCTURE: 11.255689, -16.214104 https://bit.ly/alnnfsttn')
print('Support the E2 alien invasion using:\u001b[32;1m HKSDN9BQFD')
print('\u001b[0m')
