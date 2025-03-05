from data_model_orm import DataModel, Field
from typing import Optional

from .base import ENGINE


class ParentCategory(DataModel, table=True):
    """
    ParentCategory model representing a parent category entity in the system.
    """

    __engine__ = ENGINE

    parent_category_id: Optional[int] = Field(
        primary_key=True, description="The unique identifier for the parent category"
    )
    name: str = Field(description="The name of the parent category")
    description: Optional[str] = Field(
        description="The description of the parent category"
    )
