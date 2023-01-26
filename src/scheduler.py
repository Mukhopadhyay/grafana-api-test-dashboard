"""
Scheduling the API Tests
"""
import time

import schedule

from core import oss

# Scheduling stuff
# schedule.every(3).minutes.do(oss.osrm_route)
schedule.every(3).seconds.do(oss.osrm)


# Driver code
if __name__ == "__main__":

    # Adding the DBs in the database

    while True:
        schedule.run_pending()
        time.sleep(1)
