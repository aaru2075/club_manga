env_vars = {
  # Get From my.telegram.org
  "API_HASH": "e9bfc473049cbaeff901ca6892d559c7",
  # Get From my.telegram.org
  "API_ID": "20373005",
  #Get For @BotFather
  "BOT_TOKEN": "8012002306:AAHjjsEjx0KJPflbSALKkQFT7WHrKYiUGYc",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres:loBlBY3dhFENtyIo@negatively-soothed-labrador.data-1.use1.tembo.io:5432/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MC] [{chap_num}] {chap_name} @ManhwaClubbup"  

}
dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
