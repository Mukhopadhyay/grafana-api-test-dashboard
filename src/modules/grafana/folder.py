from errors.exceptions import GrafanaHTTPError
from modules.grafana import utils as grafana_utils
from utils import http


async def create_folder(title: str):
    data = {"title": title, "uid": "_".join(title.casefold().split())}
    r, _, _, status = await http.post_async(grafana_utils.get_folder_url(), data=data)
    if status != 200:
        raise GrafanaHTTPError("Could not create a folder", status_code=status, data=r)
    return r
