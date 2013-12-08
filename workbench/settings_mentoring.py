from settings import *

LOAD_SCENARIOS_FROM = ('mentoring', 'mentoring-table', 'mentoring-dataexport')
INSTALLED_APPS += ('mentoring',)

DATABASES['default']['NAME'] = 'workbench.sqlite'

LOGGING['formatters'] = {
    'normal': {
        'format': '[%(asctime)s] %(levelname)s (%(module)s): %(message)s'
    }
}
LOGGING['handlers']['console'] = {
    'level':'DEBUG',
    'class':'logging.StreamHandler',
    'formatter': 'normal'
}
LOGGING['loggers'][''] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': True,
}
