import logging
from fastapi import FastAPI, HTTPException, Query
from linked_list import LinkedList

# Configure logging
logging.basicConfig(filename="app.log", filemode="a", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()
linked_list = LinkedList()


@app.get("/")
def read_root():
    logging.info("Root endpoint accessed.")
    return {"message": "Welcome to the Linked List API!"}


@app.get("/get-data/")
def get_data():
    """Retrieve all data from the linked list."""
    data = linked_list.get_data()
    if not data:
        logging.warning("Linked list is empty.")
        raise HTTPException(status_code=404, detail="Linked list is empty.")
    logging.info("Data retrieved successfully.")
    return {"linked_list": data}


@app.post("/add-at-beginning/")
def add_at_beginning(data: str = Query(None)):
    """Add a node at the beginning of the linked list."""
    if not data:
        logging.error("Attempt to add empty data at the beginning.")
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.add_at_beginning(data)
    logging.info(f"Successfully added data at the beginning: {data}")
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str = Query(None)):
    """Add a node at the end of the linked list."""
    if not data:
        logging.error("Attempt to add empty data at the end.")
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.add_at_end(data)
    logging.info(f"Successfully added data at the end: {data}")
    return {"message": message}


@app.put("/update-node/")
def update_node(old_data: str = Query(None), new_data: str = Query(None)):
    """Update a node's value in the linked list."""
    if not old_data or not new_data:
        logging.error("Empty old data or new data provided for update.")
        raise HTTPException(status_code=400, detail="Old data and new data cannot be empty.")
    message = linked_list.update_node(old_data, new_data)
    if "not found" in message.lower():
        logging.warning(f"Failed to update: {message}")
        raise HTTPException(status_code=404, detail=message)
    logging.info(f"Successfully updated node: {old_data} to {new_data}")
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str = Query(None)):
    """Delete a node from the linked list."""
    if not data:
        logging.error("Attempt to delete a node with empty data.")
        raise HTTPException(status_code=400, detail="Data cannot be empty.")
    message = linked_list.delete_node(data)
    if "not found" in message.lower():
        logging.warning(f"Failed to delete: {message}")
        raise HTTPException(status_code=404, detail=message)
    logging.info(f"Successfully deleted node: {data}")
    return {"message": message}
