import zoneinfo
import pandas as pd
import psycopg2
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import zoneinfo

class Config:
    
    JOBS = [
        {
            "id": "id",
            "func": "jobs:script",
            "args": (1, 2),
            "trigger": "interval",
            "seconds": 10,
        }
    ]
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "Europe/Paris"  


def script():
    conn = psycopg2.connect(
            host="localhost",
            database="test",
            user="utilisateur",
            password="root")
		
    cur = conn.cursor()

    query = "SELECT * FROM lotissement WHERE balcony = 'True'; "
    balcony = pd.read_sql_query(query, conn)
    print('The time is: %s' % datetime.now())
    balcony.to_excel("balcony.xlsx", index=False, encoding="UTF-8")


scheduler = BackgroundScheduler()
scheduler.add_job(script, 'interval', minutes=55)
scheduler.start()