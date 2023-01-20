"""
This is where your test goes
"""
import asyncio

from database import utils as db_utils
from models.response import Response
from utils import http

GET_URLS = (
    "http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false",
)


def osrm_route():
    print("OSRM ROUTE CALLED!")
    name = "OSRM"
    url = GET_URLS[0]
    version = "v1"
    category = "GEO"
    (resp, elapsed, con_len, stat) = asyncio.run(http.get_async(url))
    data = Response(
        name=name, url=url, elapsed=elapsed, version=version, category="GEO", status_code=stat, content_length=con_len
    )
    r = db_utils.insert_into_endpoint(data)
    print(r)
