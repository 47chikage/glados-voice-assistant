import requests
from bs4 import BeautifulSoup

def save_html():
    URL = "https://theportalwiki.com/wiki/GLaDOS_voice_lines"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    with open('html/website.html', 'w') as file:
        file.write(soup.prettify())

filters=['rank','pick','ban','battle','double','triple','mega','quintuple','hero','ancient','dota','barracks','Radiant','Dire','megacreeps','top','bottom','Moby-Dick','Player','test',"Aperture",'lab','middle','top','bottom','right']

def check_filters(voiceline,filters):
    for x in filters:
        voiceline,x=voiceline.lower(),x.lower()
        if x in voiceline:
            return False
    return True
def extract_data():
    dump_text=[]
    with open('html/website.html', 'r') as file:
        soup=BeautifulSoup(file.read(),'lxml')
        soup=soup.find('div',{"id": "bodyContent"})
        for voiceline in soup.find_all('i'):
            voiceline=voiceline.get_text()
            if check_filters(voiceline,filters):
                dump_text.append(voiceline.replace('  ','').replace('\n',''))
        with open('voicelines2.txt','w') as file:
            file.write('\n'.join(dump_text))
extract_data()