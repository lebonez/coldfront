from coldfront.config.base import INSTALLED_APPS, ENV

#------------------------------------------------------------------------------
# Enable XDMoD support
#------------------------------------------------------------------------------
INSTALLED_APPS += [
    'coldfront.plugins.xdmod',
]

XDMOD_API_URL = ENV.str('COLDFRONT_PLUGIN_XDMOD_API_URL')