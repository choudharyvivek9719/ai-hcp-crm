"""
CRUD package for AI Healthcare CRM.

This package contains all database operations for the application.

Modules:
    - user.py         : CRUD operations for Sales Representatives
    - hcp.py          : CRUD operations for Healthcare Professionals (HCPs)
    - interaction.py  : CRUD operations for HCP Interactions
    - followup.py     : CRUD operations for Follow-up records
"""

from .user import *
from .hcp import *
from .interaction import *
from .followup import *

__all__ = [
    "create_user",
    "get_user",
    "get_all_users",
    "update_user",
    "delete_user",

    "create_hcp",
    "get_hcp",
    "get_all_hcps",
    "update_hcp",
    "delete_hcp",

    "create_interaction",
    "get_interaction",
    "get_all_interactions",
    "update_interaction",
    "delete_interaction",

    "create_followup",
    "get_followup",
    "get_all_followups",
    "update_followup",
    "delete_followup",
]
