import zoneinfo
import pandas as pd
import psycopg2
from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import zoneinfo
import pytz

#Paris = zoneinfo.ZoneInfo("Europe/Paris")


def script():
    conn = psycopg2.connect(
            host="localhost",
            database="test",
            user="utilisateur",
            password="root")
		
    cur = conn.cursor()

    query = "SELECT * FROM lotissement WHERE balcony = 'True'; "
    balcony = pd.read_sql_query(query, conn)
    #print('The time is: %s' % datetime.now(tzinfo=Paris))
    balcony.to_excel("balcony.xlsx", index=False, encoding="UTF-8")

def tick():
    print('The time is: %s' % datetime.now())

scheduler = BlockingScheduler()
scheduler.add_job(tick, 'interval', seconds=10, timezone="Europe/Paris", start_date= datetime.now())
scheduler.start() 