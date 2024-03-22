from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
ADMINS = list(map(int, env.list("ADMINS")))
THROTTLING_RANGE = env.float("THROTTLING_RANGE")
