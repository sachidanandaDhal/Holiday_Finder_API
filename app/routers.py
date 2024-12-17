from fastapi import APIRouter, HTTPException
from app.models import NodeData, UpdateNodeData, LinkedListResponse
from app.linked_list import LinkedList

linked_list = LinkedList()

router = APIRouter()

@router.get("/", summary="Root endpoint", description="Returns a welcome message.")
def read_root():
    return {"message": "Welcome to the Linked List API!"}

@router.get("/list", response_model=LinkedListResponse, summary="Get all nodes", description="Retrieve all nodes in the linked list.")
def get_linked_list():
    nodes = linked_list.to_list()
    return LinkedListResponse(nodes=nodes)

@router.post("/list/add/beginning", summary="Add node at the beginning", description="Adds a node with specified value at the beginning of the linked list.")
def add_node_at_beginning(data: NodeData):
    linked_list.add_at_beginning(data.value)
    return {"message": f"Node with value {data.value} added at the beginning."}

@router.post("/list/add/end", summary="Add node at the end", description="Adds a node with specified value at the end of the linked list.")
def add_node_at_end(data: NodeData):
    linked_list.add_at_end(data.value)
    return {"message": f"Node with value {data.value} added at the end."}

@router.put("/list/update", summary="Update a node", description="Update the value of a node in the linked list.")
def update_node(data: UpdateNodeData):
    updated = linked_list.update_node(data.target_value, data.new_value)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Node with value {data.target_value} not found.")
    return {"message": f"Node with value {data.target_value} updated to {data.new_value}."}

@router.delete("/list/delete/{value}", summary="Delete a node", description="Delete a node by its value from the linked list.")
def delete_node(value: int):
    deleted = linked_list.delete_node(value)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Node with value {value} not found.")
    return {"message": f"Node with value {value} deleted."}
