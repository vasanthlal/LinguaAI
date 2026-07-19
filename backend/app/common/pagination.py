from sqlalchemy.orm import Query


def paginate(
    query: Query,
    skip: int = 0,
    limit: int = 10,
):
    """
    Apply pagination to a SQLAlchemy query.
    """

    return (
        query
        .offset(skip)
        .limit(limit)
    )