"""
This is where we create dictionaries for all the endpoints
"""
from schemas.db import Api
from typing import List, Dict

# This is going to be initialized in the database
apis: List[Dict[str, Api]] = {
    'OSRM': Api(
        name="OSRM",
        url="http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false",
        method="GET",
        version="v1",
        category="GEO",
        description="Open source routing machine."
    ),
    'RandomUser': Api(
        name="RandomUser",
        url="https://randomuser.me/api/",
        method="GET",
        category="Random Data",
        description="A free open source API for generating random user data."
    ),
    "JSONPlaceHolder": Api(
        name="JSONPlaceHolder",
        url="http://jsonplaceholder.typicode.com/posts",
        method="GET",
        category="Random JSON Data",
        description="Free fake API for testing and prototyping"
    )
}
