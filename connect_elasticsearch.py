import elasticsearch
import requests
import creds
import json
from elasticsearch import Elasticsearch

server = creds.elasticsearch_server
print(elasticsearch.__version__)
es = Elasticsearch(creds.elasticsearch_server)
print(es.ping())

# es.indices.create(index="bible")
print(es.indices.exists(index="bible"))

print(es.indices.get_alias(index="*"))

# table = "/movies"
# headers = {'Content-Type': 'application/json'}

#--------------------------------------
# THIS WORKS
# resp = requests.get(server)

# print(resp.text)

#--------------------------------------

# this will give information about the indices of the elasticsearch
# param = (('v', ''),)
# resp = requests.get(f'{server}/_cat/indices', params=param)
# print(resp.text)

#--------------------------------------

# this will attempt to put a mapping to the elasticsearch

# data = {
#     "mappings": {
#         "properties": {
#             "year": {
#                 "type": "date"
#             }
#         }
#     }
# }

# jdata = json.dumps(data)
# ser_table = server+table

# print(ser_table)
# resp = requests.put(server+table, headers=headers, data=jdata)

# print(resp.text)

#----------------------------------------
# table = "/shakespeare"
# elastic_url_switch = "/_search?pretty"

# data = {
#     "query": {
#         "match_phrase": {
#             "text_entry": "but soft"
#         }
#     }
# }

# jdata = json.dumps(data)
# resp = requests.get(server+table+elastic_url_switch, headers=headers, data=jdata)
# print(resp.text)

#----------------------------------------

# Create new index
# server = creds.elasticsearch_server
# table = "/bible"
# headers = {'Content-Type': 'application/json'}

#----------------------------------------

# Fix yellow status if replicas > 0

