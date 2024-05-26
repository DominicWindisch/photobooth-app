"""Example 2nd-level subpackage."""

from fastapi import APIRouter, Depends

from ..auth_dependencies_bearer import get_current_active_user
from . import auth, config, files, information

__all__ = [
    "auth",
    "config",  # refers to the 'config.py' file
    "files",
    "information",
]

router = APIRouter(prefix="/api/admin")
router.include_router(auth.router)
router.include_router(config.router, dependencies=[Depends(get_current_active_user)])
router.include_router(files.router, dependencies=[Depends(get_current_active_user)])
router.include_router(information.router, dependencies=[Depends(get_current_active_user)])
