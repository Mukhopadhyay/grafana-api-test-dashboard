import json
import pytest

@pytest.mark.schema
def test_endpoint_models(endpoint_keys):
    pyd, orm = endpoint_keys

    for x in pyd:
        assert x in orm
