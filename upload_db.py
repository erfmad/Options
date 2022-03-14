import sqlite3
import alpaca_trade_api as tradeapi # check their api

connection = sqlite3.connect('app.db')
connection.row_factory = sqlite3.Row # what this does whenever we query it returns sqlite objects which it helps when we wanna call row feature instead of row[0] say row['symbol']

cursor = connection.cursor()

cursor.execute("""
    SELECT symbol,company FROM stock
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

api = tradeapi.REST('PKTAQ9ZXE9D3GMC9ABMO','2qQJnNrXMxTl8LoPf1Q5JwcoMCMtZji4iXa4n0DR',base_url='https://paper-api.alpaca.markets')
assets = api.list_assets()

#for asset in assets:
#    try:
#        if asset.status == 'active' and asset.tradable:
#            cursor.execute("INSERT INTO stock (symbol,company) VALUES (?,?)",(asset.symbol,asset.name))
#    except Exception as e:
#        print(asset.symbol)
#        print(e)


connection.commit()
