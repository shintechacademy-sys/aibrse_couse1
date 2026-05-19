from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

@app.post("/products/available")
def get_available_products(payload: Dict):
    # Parse input -> Product objects
    products_input = payload.get("products", [])
    products = [
        Product(
            id=p["id"],
            name=p["name"],
            stock=p["stock"],
            is_active=p["is_active"]
        )
        for p in products_input
    ]

    # Gọi hàm đã định nghĩa
    available_products = filter_available(products)

    # Convert output
    return {
        "products": [p.to_dict() for p in available_products]
    }


if __name__ == "__main__":
    import uvicorn
    from product import Product, filter_available
    uvicorn.run(app, host="0.0.0.0", port=8000)




