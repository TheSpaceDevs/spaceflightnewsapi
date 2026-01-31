from environs import Env

env = Env()
env.read_env()

bind = ":8000"

# https://blog.graywind.org/posts/gunicorn-in-containers/
workers = 1

errorlog = "-"
loglevel = "info"
accesslog = "-"

"""\
    The access log format.

    ===========  ===========
    Identifier   Description
    ===========  ===========
    h            remote address
    l            ``'-'``
    u            user name (if HTTP Basic auth used)
    t            date of the request
    r            status line (e.g. ``GET / HTTP/1.1``)
    m            request method
    U            URL path without query string
    q            query string
    H            protocol
    s            status
    B            response length
    b            response length or ``'-'`` (CLF format)
    f            referrer (note: header is ``referer``)
    a            user agent
    T            request time in seconds
    M            request time in milliseconds
    D            request time in microseconds
    L            request time in decimal seconds
    p            process ID
    {header}i    request header
    {header}o    response header
    {variable}e  environment variable
    ===========  ===========

    Use lowercase for header and environment variable names, and put
    ``{...}x`` names inside ``%(...)s``. For example::

        %({x-forwarded-for}i)s
"""
access_log_format = '%({x-forwarded-for}i)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
