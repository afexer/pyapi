from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        'simpleExample': {
            'level': 'DEBUG',
            'handlers': ['wsgi', 'console'],
            'propagate': 'no',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi', 'console']
    }
})