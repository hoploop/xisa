# PYTHON IMPORTS
import io
import logging
from bson import ObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response


# LOCAL IMPORTS
from api.routers import GetFilesystem


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)
