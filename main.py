from fastapi import FastAPI
from routes.authRoutes import auth_router
from routes.orderRoutes import order_router


app = FastAPI()
app.include_router(auth_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")

