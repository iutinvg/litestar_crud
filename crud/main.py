from .settings import Conf

import uvicorn
from litestar import Litestar, get


@get("/")
async def index() -> str:
    return f"Hello, world! {Conf.debug}"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
