from typing import AsyncGenerator

import pytest
from yarl import URL

from transformerbeeclient.client import UnauthenticatedTransformerBeeClient
from transformerbeeclient.protocols import TransformerBeeClient

_local_docker_url = URL("http://localhost:5021")


@pytest.fixture
async def unauthenticated_client() -> AsyncGenerator[TransformerBeeClient, None]:
    client = UnauthenticatedTransformerBeeClient(base_url=_local_docker_url)
    yield client
    await client.close_session()
