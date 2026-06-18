import datetime
import sys


if __name__ == '__main__':
    print('error')


_RED = '\033[31m'
_YELLOW = '\033[33m'
_GREEN = '\033[32m'
_RESET = '\033[0m'


LOG_LEVEL_ERROR = 'error'
LOG_LEVEL_INFO = 'info'
LOG_LEVEL_WARNING = 'warning'

STD_OUTPUT = 'stdout'
STD_ERROR = 'stderr'
STD_OUTPUT_ERROR = 'stdout/stderr'


def _colorize_log_type(log_type: str, formatted_type: str) -> str:
    title = ''
    if log_type.lower() == 'error':
        title = _RED + formatted_type + _RESET
    elif log_type.lower() == 'info':
        title = _GREEN + formatted_type + _RESET
    elif log_type.lower() == 'warning':
        title = _YELLOW + formatted_type + _RESET

    return '[' + title + '] '


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
    

def _create_log_timestamp() -> str:
    return datetime.datetime.now().ctime()


def _validate_standard_stream(standard_stream: str) -> None:
    if standard_stream not in (STD_ERROR, STD_OUTPUT, STD_OUTPUT_ERROR):
        raise ValueError(f'Invalid standard stream: {standard_stream}')


def _redirect_log(log_string: str, standard_stream: str) -> None:

    log_string += '\n'

    if standard_stream == STD_OUTPUT:
        sys.stdout.write(log_string)
        sys.stdout.flush()
    elif standard_stream == STD_ERROR:
        sys.stderr.write(log_string)
        sys.stderr.flush()
    elif standard_stream == STD_OUTPUT_ERROR:
        sys.stdout.write(log_string)
        sys.stdout.flush()
        sys.stderr.write(log_string)
        sys.stderr.flush()


def print_log(log_level: str, 
              message: str, 
              is_colored: bool = False, 
              is_timestamp: bool = False, 
              standard_stream=STD_OUTPUT) -> None:
    """
    Creates logs for stdout

    Args:
        log_level (str): define levels of log: 'error', 'info' and 'warning'
        message (str): an informative message for end user
        is_colored (bool): if it sets to True, the log status will be green
        is_timestamp (bool): if it sets to True, the timestamp will be presented in log message
        standard_stream (str): it will direct the log to stdout, stderr or both

    Returns:
        (None)
    
    .. note::
        It is not suggested to use is_colored=True if stderr (STD_ERROR) is used, especially if the log is going
        to be read by machines

    Examples:
        >>> print_log(LOG_LEVEL_INFO, 'this is a message')
        [  info:   ] this is a message
    """
    _validate_standard_stream(standard_stream)

    log_string = ''
    if is_timestamp:
        log_string  = _create_log_timestamp() + ' - '

    if is_colored:
        log_string = _create_header(log_level, is_colored) + log_string + message
    else:
        log_string = _create_header(log_level) + ' ' + log_string + message

    _redirect_log(log_string=log_string, standard_stream=standard_stream)
