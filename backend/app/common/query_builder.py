from typing import Any

from sqlalchemy import asc, desc


def apply_sorting(
    query,
    sortable_columns: dict[str, Any],
    sort_by: str,
    order: str,
):
    """
    Apply sorting to a SQLAlchemy query.
    """

    column = sortable_columns.get(sort_by)

    if column is None:
        return query

    if order.lower() == "desc":
        return query.order_by(desc(column))

    return query.order_by(asc(column))