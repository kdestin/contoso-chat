import sys
from pathlib import Path

import pytest
from azure.identity import DefaultAzureCredential
from promptflow.client import PFClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from .. import chat_request


@pytest.fixture()
def pf() -> PFClient:
    return PFClient(credential=DefaultAzureCredential())


def test_direct_invocation() -> None:
    chat_request.main()


def test_sample_as_flow(pf: PFClient) -> None:
    pf.test(
        flow=Path(__file__).resolve().parent.parent / "flow.flex.yaml",
        inputs={
            "customerId": 4,
            "question": "What hiking jackets would you recommend?",
            "chat_history": [],
        },
    )
