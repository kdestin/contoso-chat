import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from .. import chat_request


def test_direct_invocation() -> None:
    chat_request.main()
