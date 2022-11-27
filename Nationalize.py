import requests

def national(name):
    response = requests.get(f"https://api.nationalize.io/?name={name}")
    re_no = (response.status_code)

    if re_no == 200:    
        re = response.json()['country']
        print(f"{name} you're from..\n")
        for co in re:        
            country = co['country_id']
            country_code = requests.get(f"https://restcountries.com/v2/alpha/{country}")
            try:
                country_name = country_code.json()['name']
            except KeyError:
                country_name = country              
            probability = co['probability']
            pro = round(probability*100, 2)
            print(f"{country_name}: {pro}% ")
    else:
        print('Error Happend..')        

national('theekshana') #name
