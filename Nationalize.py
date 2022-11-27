import requests
import json 

def national(name):
    response = requests.get(f"https://api.nationalize.io/?name={name}")
    re_no = (response.status_code)    
    re2 = json.load(open('countries.json'))   

    if re_no == 200:    
        re = response.json()['country']
        print(f"{name} you're from..\n")
        for co in re:        
            country = co['country_id']            
            try:
                country_name = re2[""+country+""]
            except KeyError:
                country_name = country              
            probability = co['probability']
            pro = round(probability*100, 2)
            print(f"{country_name}: {pro}% ")
    else:
        print('Error Happend..')        

national('theekshana') #name
