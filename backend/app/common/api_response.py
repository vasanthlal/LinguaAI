from typing import Any


class APIResponse:
    @staticmethod
    def success(
        data: Any = None,
        message: str = "Success",
    ):
        return {
            "success": True,
            "message": message,
            "data": data,
        }

    @staticmethod
    def error(
        message: str,
        code: int,
    ):
        return {
            "success": False,
            "error": {
                "code": code,
                "message": message,
            },
        }