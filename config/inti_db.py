import sys
import os

# This line ensures your project root is in the Python path so imports work perfectly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import engine, Base
# Change the relative import (..) to an absolute import from the root
from models.userModel import User, Order 

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
