from pytagcloud import create_tag_image, make_tags, LAYOUT_MIX
import simplejson as json
import requests

response = requests.get("https://api.github.com/repos/apache/libcloud/contributors")
contributors = response.json()
weight=[]
for contributor in contributors:
    weight.append(('@' + contributor['login'], int(contributor['contributions'])))
tags = make_tags(weight[:100], minsize=50, maxsize=230)
create_tag_image(tags, 'tags.png', size=(1500,1500), layout=LAYOUT_MIX, fontname='Molengo', rectangular=True)
import webbrowser
webbrowser.open('tags.png') # see results