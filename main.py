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


# @app.post("/add-at-beginning/")
# def add_at_beginning(data: str = Query(None)):
#     """Add a node at the beginning of the linked list."""
#     if not data:
#         logging.error("Attempt to add empty data at the beginning.")
#         raise HTTPException(status_code=400, detail="Data cannot be empty.")
#     message = linked_list.add_at_beginning(data)
#     logging.info(f"Successfully added data at the beginning: {data}")
#     return {"message": message}


# @app.post("/add-at-end/")
# def add_at_end(data: str = Query(None)):
#     """Add a node at the end of the linked list."""
#     if not data:
#         logging.error("Attempt to add empty data at the end.")
#         raise HTTPException(status_code=400, detail="Data cannot be empty.")
#     message = linked_list.add_at_end(data)
#     logging.info(f"Successfully added data at the end: {data}")
#     return {"message": message}

@app.post("/add-at-beginning/")
def add_at_beginning(data: str = Query(None)):
    """Add a node at the beginning of the linked list."""
    if not data:
        logging.error("Attempt to add empty data at the beginning.")
        raise HTTPException(status_code=400, detail="Error: Data cannot be empty.")
    try:
        int_data = int(data)
    except ValueError:
        logging.error(f"Non-integer data provided: {data}")
        raise HTTPException(status_code=400, detail="Error: Only integer values are allowed.")
    try:
        message = linked_list.add_at_beginning(int_data)
    except ValueError as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"Successfully added data at the beginning: {int_data}")
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str = Query(None)):
    """Add a node at the end of the linked list."""
    if not data:
        logging.error("Attempt to add empty data at the end.")
        raise HTTPException(status_code=400, detail="Error: Data cannot be empty.")
    try:
        int_data = int(data)
    except ValueError:
        logging.error(f"Non-integer data provided: {data}")
        raise HTTPException(status_code=400, detail="Error: Only integer values are allowed.")
    try:
        message = linked_list.add_at_end(int_data)
    except ValueError as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"Successfully added data at the end: {int_data}")
    return {"message": message}




# @app.put("/update-node/")
# def update_node(old_data: str = Query(None), new_data: str = Query(None)):
#     """Update a node's value in the linked list."""
#     if not old_data or not new_data:
#         logging.error("Empty old data or new data provided for update.")
#         raise HTTPException(status_code=400, detail="Old data and new data cannot be empty.")
#     message = linked_list.update_node(old_data, new_data)
#     if "not found" in message.lower():
#         logging.warning(f"Failed to update: {message}")
#         raise HTTPException(status_code=404, detail=message)
#     logging.info(f"Successfully updated node: {old_data} to {new_data}")
#     return {"message": message}


# @app.delete("/delete-node/")
# def delete_node(data: str = Query(None)):
#     """Delete a node from the linked list."""
#     if not data:
#         logging.error("Attempt to delete a node with empty data.")
#         raise HTTPException(status_code=400, detail="Data cannot be empty.")
#     message = linked_list.delete_node(data)
#     if "not found" in message.lower():
#         logging.warning(f"Failed to delete: {message}")
#         raise HTTPException(status_code=404, detail=message)
#     logging.info(f"Successfully deleted node: {data}")
#     return {"message": message}



@app.put("/update-node/")
def update_node(old_data: str = Query(None), new_data: str = Query(None)):
    """Update a node's value in the linked list."""
    if not old_data or not new_data:
        logging.error("Empty old data or new data provided for update.")
        raise HTTPException(status_code=400, detail="Error: Old data and new data cannot be empty.")
    try:
        old_data_int = int(old_data)
        new_data_int = int(new_data)
    except ValueError:
        logging.error(f"Non-integer data provided: old_data={old_data}, new_data={new_data}")
        raise HTTPException(status_code=400, detail="Error: Only integer values are allowed.")
    message = linked_list.update_node(old_data_int, new_data_int)
    if "not found" in message.lower():
        logging.warning(f"Failed to update: {message}")
        raise HTTPException(status_code=404, detail=message)
    logging.info(f"Successfully updated node: {old_data_int} to {new_data_int}")
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str = Query(None)):
    """Delete a node from the linked list."""
    if not data:
        logging.error("Attempt to delete a node with empty data.")
        raise HTTPException(status_code=400, detail="Error: Data cannot be empty.")
    try:
        data_int = int(data)
    except ValueError:
        logging.error(f"Non-integer data provided: {data}")
        raise HTTPException(status_code=400, detail="Error: Only integer values are allowed.")
    message = linked_list.delete_node(data_int)
    if "not found" in message.lower():
        logging.warning(f"Failed to delete: {message}")
        raise HTTPException(status_code=404, detail=message)
    logging.info(f"Successfully deleted node: {data_int}")
    return {"message": message}


@app.post("/reverse/")
def reverse_linked_list():
    """Reverse the linked list."""
    try:
        logging.info(f"linked_list type: {type(linked_list)}")
        reversed_list = linked_list.reverse_linked_list()
        
        # Get the reversed data from the new reversed linked list
        reversed_data = reversed_list.get_data()
        logging.info("Linked list reversed successfully.")
        return {"message": "Linked list reversed successfully.",
                "reversed_data": reversed_data}
    except Exception as e:
        logging.error(f"Error while reversing linked list: {str(e)}")
        raise HTTPException(status_code=500, detail="Error reversing the linked list.")

@app.post("/sort/")
def sort_linked_list():
    """Sort the linked list and return the sorted data."""
    try:
        # Sort the linked list using sorted_linked_list method
        sorted_list = linked_list.sorted_linked_list()
        
        # Get the sorted data from the new sorted linked list
        sorted_data = sorted_list.get_data()
        
        logging.info("Linked list sorted successfully.")
        
        # Return the response with the sorted data
        return {
            "message": "Linked list sorted successfully.",
            "sorted_data": sorted_data
        }
        
    except Exception as e:
        logging.error(f"Error while sorting linked list: {str(e)}")
        raise HTTPException(status_code=500, detail="Error sorting the linked list.")


