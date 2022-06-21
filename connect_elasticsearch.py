import requests
import creds

server = creds.elasticsearch_server
conn = requests.get(server)

print(conn.text)
