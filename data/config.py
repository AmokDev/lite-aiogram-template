from environs import Env

env = Env()
env.read_env()

token = env.str("TOKEN")
admins = list(map(int, env.list("ADMINS")))
throttling_range = env.float("THROTTLING_RANGE")
