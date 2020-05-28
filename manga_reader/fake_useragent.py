import requests
from bs4 import BeautifulSoup
from random import choice,randint
import urllib3
def get_user_agent():
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(f'https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/{randint(1,11)}',verify = False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,'html.parser')

            user_agent_table = soup.find('table',{'class' : 'table-useragents'})

            td = user_agent_table.findChildren('td',{'class' : 'useragent'})

            user_agent_list = [user_agent.text for user_agent in td]
            return {'User-Agent':choice(user_agent_list)}
    except Exception as ex:
        print(ex)        
#user_agent = get_user_agent()    
#print(user_agent)