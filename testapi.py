import  requests


data= {
        "country_name": "ajjei",
        "total_cases": "117,710",
        "new_cases": 5645,
        "new_death": 587,
        "total_death": "10,935",
        "total_recover": "30,513",
        "active-cases": "76,262",
        "total_case_per_minion_pop": "2,518",
        "total_death_per_minion_pop": "234"
    }
import json
url='http://127.0.0.1:8000/api/create_data/'
headers={
'Authorization':'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InR6MDF4IiwiZXhwIjoxNTg2NTIzNTY3LCJlbWFpbCI6ImFiZHVyOTYzcmFobWFuQGdtYWlsLmNvbSJ9.q9EDZfJB5mIv717N64VvucDK-TGwQvlO4W4Ww4pJGiY'
}
# res=requests.post(url,data,headers=headers)
res=requests.get('http://127.0.0.1:8000/api/get-data/country=usa/');
print(res.json())
