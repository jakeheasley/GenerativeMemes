from Login_Settings_General import Login_Settings
from SQL import SQL
import Scheduler_Initializer


def config():
    sql = SQL(host=Login_Settings.database['HOST'],
              port=Login_Settings.database['PORT'],
              username=Login_Settings.database['DB_USERNAME'],
              password=Login_Settings.database['DB_PASSWORD'],
              database=Login_Settings.database['DATABASE'])

    sql.table_setup()
    sql.close()

    Scheduler_Initializer.initialize()


if __name__ == "main":
    config()
