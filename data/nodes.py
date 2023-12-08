"""
This file contains all of the node data for the menu creation
and leafing.
"""
import dataclasses
import enum

class Statement_Type(enum):
    type = "question" or "answer"
    

@dataclasses
class Node:
    "display_text": str
    "back_links": list
    "forward_links": list
    "node_id": str
    "statement_type": Statement_Type
    

