from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
chek = (-1002082828622, "brbalokanal", 'https://t.me/abduaziztest')
