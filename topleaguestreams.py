#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import requests

r = requests.get("https://api.twitch.tv/kraken/streams?game=League+of+legends&limit=10", headers={"Accept": "application/vnd.twitchtv.v3+json"})
streams = r.json()['streams']
for stream in streams:
    info = stream['channel']
    try:
        status = info['status']
    except:
        status = "**Can't load status**"
    try: 
        print(str(stream['viewers']) + ' - ' + info['display_name'] + ' - ' + status)
    except:
        print('ERROR')
        print(info)
