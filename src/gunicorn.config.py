from multiprocessing import cpu_count

from environs import Env

env = Env()
env.read_env()

bind = ":8000"

# https://gunicorn.org/guides/docker/#running-in-background
workers = (2 * cpu_count()) + 1

errorlog = "-"
loglevel = "info"
accesslog = "-"
