import psycopg2
import datetime
from apscheduler.schedulers.background import BackgroundScheduler




def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            database="test",
            user="utilisateur",
            password="root")
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
  
    with open('Promoteur_imo.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'lotissement', sep=';', null='')

    conn.commit()
    cur.close()
    conn.close()
    print('Database connexion closed.')
    print('The time is: %s' % datetime.now())



if __name__ == '__main__':
    connect()

