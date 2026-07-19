from pydantic import BaseModel, Field


class Product(BaseModel):
    name:str
    price: float = Field(gt=0, description="The price of the product greater than 0")

product_data = {
    "name":"",
    "price":-1
}

Product(**product_data)