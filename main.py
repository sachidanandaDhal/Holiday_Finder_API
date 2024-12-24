from fastapi import FastAPI, HTTPException, Query
from linked_list import LinkedList

app = FastAPI()
linked_list = LinkedList()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Linked List API!"}


@app.get("/get-data/")
def get_data():
    """Retrieve all data from the linked list."""
    data = linked_list.get_data()
    if not data:
        raise HTTPException(status_code=404, detail="Linked list is empty.")
    return {"linked_list": data}


@app.post("/add-at-beginning/")
def add_at_beginning(data: str = Query(None)):
    """Add a node at the beginning of the linked list."""
    if not data:
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.add_at_beginning(data)
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str = Query(None)):
    """Add a node at the end of the linked list."""
    if not data:
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.add_at_end(data)
    return {"message": message}


@app.put("/update-node/")
def update_node(old_data: str =  Query(None), new_data: str= Query(None)):
    """Update a node's value in the linked list."""
    if not old_data or not new_data:
        raise HTTPException(status_code=400, detail="Old data and new data cannot be empty.")
    message = linked_list.update_node(old_data, new_data)
    if "not found" in message.lower():
        raise HTTPException(status_code=404, detail=message)
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str = Query(None)):
    """Delete a node from the linked list."""
    if not data:
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.delete_node(data)
    if "not found" in message.lower():
        raise HTTPException(status_code=404, detail=message)
    return {"message": message}
