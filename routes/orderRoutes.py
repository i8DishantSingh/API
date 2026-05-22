from fastapi import APIRouter


order_router = APIRouter(prefix="/order", tags=['order'])

@order_router.get("/getorders")
def get_orders():
    return {"messages" : "No Orders"}
