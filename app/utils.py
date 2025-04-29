from bson import ObjectId

def serialize_mongo_document(doc):
    if isinstance(doc, list):
        return [serialize_mongo_document(item) for item in doc]
    elif isinstance(doc, dict):
        return {k: serialize_mongo_document(v) for k, v in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc
