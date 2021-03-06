import sqlite3, config
import alpaca_trade_api as tradeapi # check their api

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row # what this does whenever we query it returns sqlite objects which it helps when we wanna call row feature instead of row[0] say row['symbol']

cursor = connection.cursor()

cursor.execute("""
    SELECT symbol,company FROM stock
""")
rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]
api = tradeapi.REST(config.API_KEY_ID,config.SECRET_KEY,base_url=config.API_URL)
assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock{asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol,company) VALUES (?,?)",(asset.symbol,asset.name))
    except Exception as e:
       print(asset.symbol)
       print(e)


connection.commit()
