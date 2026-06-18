if __name__ == '__main__':
    print('error')


_RED = '\033[31m'
_YELLOW = '\033[33m'
_GREEN = '\033[32m'
_RESET = '\033[0m'


def _colorize_log_type(log_type: str, formatted_type: str) -> str:
    title = ''
    if log_type.lower() == 'error':
        title = _RED + formatted_type + _RESET
    elif log_type.lower() == 'info':
        title = _GREEN + formatted_type + _RESET
    elif log_type.lower() == 'warning':
        title = _YELLOW + formatted_type + _RESET

    return '[' + title + ']'


def _create_header(log_type: str, is_colored=False) -> str:
    if log_type in ('error', 'info', 'warning'):
        temp_type_string = log_type.lower() + ':'
        formatted_type = temp_type_string.center(10)

        if is_colored:
            return _colorize_log_type(log_type=log_type,
                                      formatted_type=formatted_type)
        else:
            return '[' + formatted_type + ']'
    else:
        raise ValueError('valid error types: error, info and warning')


def log_error(message: str, is_colored=False):
    """
    Creates error logs for stdout

    Args:
        message (str): an error message for end user
        is_colored (bool): if it sets to True, the log status will be red

    Returns:
        (None)

    Examples:
        >>> log_error('this is a message')
        [  error:  ] this is a message
    """
    if is_colored:
        print(_create_header('error', True) + ' ' + message)
    else:
        print(_create_header('error') + ' ' + message)


def log_info(message: str, is_colored=False):
    """
    Creates information logs for stdout

    Args:
        message (str): an informative message for end user
        is_colored (bool): if it sets to True, the log status will be green

    Returns:
        (None)

    Examples:
        >>> log_info('this is a message')
        [  info:   ] this is a message
    """
    if is_colored:
        print(_create_header('info', True) + ' ' + message)
    else:
        print(_create_header('info') + ' ' + message)


def log_warning(message: str, is_colored=False):
    """
    Creates warning logs for stdout

    Args:
        message (str): a warning message for end user
        is_colored (bool): if it sets to True, the log staus will be yellow

    Returns:
        (None)

    Examples:
        >>> log_warning('this is a message')
        [ warning: ] this is a message
    """
    if is_colored:
        print(_create_header('warning', True) + ' ' + message)
    else:
        print(_create_header('warning') + ' ' + message)
