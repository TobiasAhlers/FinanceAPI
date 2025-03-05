from data_model_orm import DataModel, Field
from typing import Optional

from .base import ENGINE


class Category(DataModel, table=True):
    """
    Category model representing a category entity in the system.
    """

    __engine__ = ENGINE

    category_id: Optional[int] = Field(
        primary_key=True, description="The unique identifier for the category"
    )
    name: str = Field(description="The name of the category")
    description: Optional[str] = Field(description="The description of the category")
    parent_id: Optional[int] = Field(
        description="The parent category id",
        foreign_key="parentcategory.parent_category_id",
    )
