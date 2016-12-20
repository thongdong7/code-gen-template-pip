# encoding=utf-8


def _install(params):
    """
    Called when install template

    :return:
    :rtype:
    """
    return {
        'data': {
            'abc': 'def'
        }
    }


def to_underscore(text):
    return text.replace('-', '_')


def lib_name(params):
    project_name = params['project_name']
    return to_underscore(project_name.replace('python-', ''))


filters = {
    'to_underscore1': to_underscore,
}

vars_decor = {
    'lib_name': lib_name
}
