from mpd import MPDClient

def connectClient(config):
    client = MPDClient()
        
    client.timeout = 10
    client.idletimeout = None
    try:
        client.connect(config.mpdserver, config.mpdport)
        if len(config.mpdpassword) > 0:
            client.password(config.mpdpassword)
    except Exception as e:
        print(e)

    return client