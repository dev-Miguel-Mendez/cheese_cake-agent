from typing import TypedDict, Any

class DefaultResponse(TypedDict):
    success: bool
    message: str
    data: Any | None