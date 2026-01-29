from environs import Env

env = Env()
env.read_env()

bind = ":8000"

# https://blog.graywind.org/posts/gunicorn-in-containers/
workers = 1

errorlog = "-"
loglevel = "info"
accesslog = "-"
