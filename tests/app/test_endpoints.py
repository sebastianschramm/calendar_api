from http import HTTPStatus
import pytest


@pytest.mark.parametrize("url, method, headers, expected_status",
                         [
    ('/health', 'get', {}, HTTPStatus.OK),
                         ])
async def test_endpoint(cli, url, method, headers, expected_status):
    resp = await getattr(cli, method)(url, headers=headers)
    assert resp.status == expected_status
