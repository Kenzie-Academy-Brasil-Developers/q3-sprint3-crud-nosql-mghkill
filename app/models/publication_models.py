from venv import create
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["entrega09"]



# Trabalhar com pymongo aqui!

class Post:
    def __init__(self, **kwargs):
       
        self.created_at = kwargs["created_at"]
        self.updated_at = kwargs["updated_at"]
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]

    
    def create_publication(self):
        data = self.__dict__

        set_id = db.entrega09.find_one({"id": len(list(db.entrega09.find())) + 1})

        # após delete, não deve repetir o id

        if not set_id:
            data["id"] = len(list(db.entrega09.find())) + 1 

            db.entrega09.insert_one(data)
        else:    
            count_id = 1
            for item in list(db.entrega09.find()):
                if item["id"] > 0:
                    count_id = item["id"]
            data["id"] = count_id + 2

            db.entrega09.insert_one(data)
            
    
    @staticmethod
    def get_publication():
        return db.entrega09.find()

    @staticmethod
    def update_publication(product_id: int, data: str):

        db.entrega09.update_one({"id": product_id}, {"$set": data})

        return db.entrega09.find_one({"id": product_id})
    
    @staticmethod
    def delete_publication(product_id: int):

        output = db.entrega09.find_one({"id": product_id})
    
        db.entrega09.delete_one({"id": product_id})
        
        return output
        

        