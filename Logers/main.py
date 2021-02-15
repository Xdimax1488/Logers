LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format_1': '{levelname} {message} {asctime}',
            'format_2': '{levelname} {message} {asctime} {pathname}',
            'format_3': '{levelname} {message} {asctime} {pathname} {exc_info}',
            'format_4': '{levelname} {message} {asctime} {module}'

        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },

    },
    'handlers': {
        'console_1': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_1'
        },
        'console_2': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_2'
        },
        'console_3': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_3'
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.FileHandler',
            'filename': '/Users/dmytrokurinnyi/Desktop/Новая папка/Logers/general.log',
            'formatter': 'format_4'

        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'django.utils.log.FileHandler',
            'filename': '/Users/dmytrokurinnyi/Desktop/Новая папка/Logers/errors.log',
            'formatter': 'format_3'

        },
        'file_security': {
            'class': 'django.utils.log.FileHandler',
            'filename': '/Users/dmytrokurinnyi/Desktop/Новая папка/Logers/security.log',
            'formatter': 'format_4'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_3'
        }
    },
    'loggers': {
        'django': {
            'handlers': (['console_1'], ['console_2'], ['console_3'], ['file_general']),
            'propagate': True,
        },
        'django.request': {
            'handlers': (['file_errors'], ['mail_admins']),
            'propagate': True,
        },
        'django.server': {
            'handlers': (['file_errors'], ['mail_admins']),
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
        }
    }
}
