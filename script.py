import xbmc, xbmcgui, xbmcaddon
from resources.telegram import fetch

ADDON = xbmcaddon.Addon()
# addonname = ADDON.getAddonInfo('name')

def load_telegram(settings):
    enabled = settings.getBool('telegram.isEnabled')
    if (not enabled): return []
    opts = {
        'token': settings.getString('telegram.token'), 
        'offset': settings.getInt('telegram.offset')
    }
    return fetch(opts)


def load_data():
    settings = ADDON.getSettings()
    return load_telegram(settings)

def main():
    dialog = xbmcgui.Dialog()
    items = load_data()
    selected=dialog.select("Streams", list([x['text'] for x in items]))
    if selected>=0:
      item = items[selected]
      cmd = 'StartAndroidActivity("","org.acestream.action.start_content","","acestream:?content_id=%s")' % item['acestream_id']
      xbmc.executebuiltin(cmd)

if (__name__ == '__main__'):
    main()