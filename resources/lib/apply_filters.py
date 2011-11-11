import xbmc
import xbmcaddon
from resources.lib.fileops import fileops
from resources.lib import language
from resources.lib.settings import _settings

__addon__ = xbmcaddon.Addon('script.extrafanartdownloader')
__language__ = language.get_abbrev()

class apply_filters:

    def __init__(self):
        self.settings = _settings()
        self.settings._get()

    def do_filter(self, art_type, mediatype, artwork, downloaded_artwork):
        if art_type == 'fanart':
            return self.fanart(mediatype, artwork, downloaded_artwork)
        if art_type == 'extrafanart':
            return self.extrafanart(mediatype, artwork, downloaded_artwork)
        elif art_type == 'extrathumbs':
            return self.extrathumbs(mediatype, artwork, downloaded_artwork)
        elif art_type == 'poster':
            return self.poster(mediatype, artwork, downloaded_artwork)
        elif art_type == 'seasonposter':
            return self.seasonposter(mediatype, artwork, downloaded_artwork)
        elif art_type == 'banner':
            return self.banner(mediatype, artwork, downloaded_artwork)
        elif art_type == 'seasonbanner':
            return self.banner(mediatype, artwork, downloaded_artwork)
        else: return false

    def fanart(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if self.settings.limit_artwork and 'height' in artwork and (mediatype == 'movie' and artwork['height'] < self.settings.limit_size_moviefanart) or (mediatype == 'tvshow' and artwork['height'] < self.settings.limit_size_tvshowfanart):
            reason = 'Size was to small: %s' % artwork['height'] 
            limited = True
        elif self.settings.limit_artwork and 'series_name' in artwork and self.settings.limit_notext and artwork['series_name']:
            reason = 'Has text'
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]
        
    def extrafanart(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if self.settings.limit_artwork and downloaded_artwork >= self.settings.limit_extrafanart_max:
            reason = 'Max number extrafanart reached: %s' % self.settings.limit_extrafanart_max
            limited = True
        elif self.settings.limit_artwork and 'height' in artwork and (mediatype == 'movie' and artwork['height'] < self.settings.limit_size_moviefanart) or (mediatype == 'tvshow' and artwork['height'] < self.settings.limit_size_tvshowfanart):
            reason = 'Size was to small: %s' % artwork['height'] 
            limited = True
        elif self.settings.limit_artwork and 'rating' in artwork and artwork['rating'] < self.settings.limit_extrafanart_rating:
            reason = 'Rating too low: %s' % artwork['rating']
            limited = True
        elif self.settings.limit_artwork and 'series_name' in artwork and self.settings.limit_notext and artwork['series_name']:
            reason = 'Has text'
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]

    def extrathumbs(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if downloaded_artwork >= self.settings.limit_extrathumbs_max:
            reason = 'Max number extrathumbs reached: %s' % downloaded_artwork
            limited = True
        elif self.settings.limit_extrathumbs and 'height' in artwork and artwork['height'] < int('169'):
            reason = 'Size was to small: %s' % artwork['height']
            limited = True
        return [limited, reason]
        
    def poster(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if self.settings.limit_extrathumbs and 'height' in artwork and artwork['height'] < int('169'):
            reason = 'Size was to small: %s' % artwork['height']
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]

    def seasonposter(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if self.settings.limit_extrathumbs and 'height' in artwork and artwork['height'] < int('169'):
            reason = 'Size was to small: %s' % artwork['height']
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]

    def banner(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if self.settings.limit_artwork and 'rating' in artwork and artwork['rating'] < self.settings.limit_extrafanart_rating:
            reason = 'Rating too low: %s' % artwork['rating']
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]
        
    def seasonbanner(self, mediatype, artwork, downloaded_artwork):
        limited = False
        reason = ''
        if not 'season' in artwork:
            reason = 'No season'
            limited = True
        elif self.settings.limit_artwork and 'rating' in artwork and artwork['rating'] < self.settings.limit_extrafanart_rating:
            reason = 'Rating too low: %s' % artwork['rating']
            limited = True
        elif self.settings.limit_artwork and self.settings.limit_language and 'language' in artwork and artwork['language'] != __language__:
            reason = "Doesn't match current language: %s" % xbmc.getLanguage()
            limited = True
        return [limited, reason]