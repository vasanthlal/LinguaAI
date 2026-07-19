from fastapi import HTTPException, status


class AppException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )


class NotFoundException(AppException):
    def __init__(self, resource: str):
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            f"{resource} not found",
        )


class BadRequestException(AppException):
    def __init__(self, message: str):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            message,
        )


class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            status.HTTP_401_UNAUTHORIZED,
            "Unauthorized",
        )


class ForbiddenException(AppException):
    def __init__(self):
        super().__init__(
            status.HTTP_403_FORBIDDEN,
            "Forbidden",
        )