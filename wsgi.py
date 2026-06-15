"""WSGI entry point for production servers."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from config import ProductionConfig

app = create_app(ProductionConfig)