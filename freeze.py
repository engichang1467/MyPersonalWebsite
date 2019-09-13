from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

# Frozen-Flask freezes my application and only have static files on my computer