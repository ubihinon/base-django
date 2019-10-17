# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).parent.parent
