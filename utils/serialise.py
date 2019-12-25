def serialise_document(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


def response(data, status):
    if status:
        return {"data": data, "status": "success"}
    else:
        return {"error": data, "status": "error"}
