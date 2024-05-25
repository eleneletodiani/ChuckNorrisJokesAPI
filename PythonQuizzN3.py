import requests
import json
resp = requests.get('http://api.chucknorris.io/jokes/random')
print('status code:', resp.status_code)
print('headers:', resp.headers)
json_result = resp.json()
res = json.loads(json_result)
res_structured = json.dumps(res, indent=4)
print(res_structured)
jokes = res['value']
print('CHuck Norris joke:', jokes)
#შევქმენი ცხრილი,სადაც შეინახება ჩაკ ნორისის ხუმრობები :)
import sqlite3
conn = sqlite3.connect('ChuckNorris_jokes.db')
c = conn.cursor()
c.execute(''' CREATE TABLE  ChuckNorris_jokes
          (jokes VARCHAR(300)''')
c.execute('INSERT INTO ChuckNorris_jokes (jokes) VALUES (?)',(jokes,))
conn.commit()
conn.close()




