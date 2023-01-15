# This essentially schedules the api calls
import time
import schedule
from core import oss

schedule.every(3).seconds.do(oss.osrm_route)

while True:
    schedule.run_pending()
    time.sleep(1)
