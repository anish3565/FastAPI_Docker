def save_in_db(db, data):
    """
    Save data to the database.

    :param db: Database connection object
    :param data: Data to be saved
    """
    try:
        db.insert(data)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error saving data: {e}")

def demo_save_in_db(data):
    return "Data Saved successfully!"