from flask import jsonify, request
from json import load
from dotenv import load_dotenv
from http import HTTPStatus
from app.models.publication_models import Post

load_dotenv()

# Desenvolver a lógica das rotas aqui

def register_one_publication():
    # chamar a class 

    data = request.get_json()

    allowed_list_keys = ["created_at", "updated_at", "title", "author", "tags", "content"]

    try:

        keys = data.keys()
        for key in keys:
            if key not in allowed_list_keys:
                return {"error": "It is not processing the request because it is malformed or possibly incorrect."}, HTTPStatus.BAD_REQUEST

        output = Post(**data)
        
        output.create_publication()

        output.__dict__.pop("_id")

    except KeyError:
        return {"error": "It is not processing the request because it is malformed or possibly incorrect."}, HTTPStatus.BAD_REQUEST

    return output.__dict__, HTTPStatus.CREATED


def get_all_publication():

    output = list(Post.get_publication())
    for dict in output:
        dict.pop("_id")

    return jsonify(output), HTTPStatus.OK


def filter_publication(product_id):
       
    output = list(Post.get_publication())

    item_id_output = {}
    for dict in output:
        if int(product_id) == int(dict["id"]):
            dict.pop("_id")
            item_id_output = dict
    if item_id_output:
        return item_id_output, HTTPStatus.OK
    
    return {"error": "Requested resource does not exist."}, HTTPStatus.NOT_FOUND
   

def update_one_publication(product_id):

    data = request.get_json()
    try:
        if len(data) == 1:
            
            allowed_list_keys = ["created_at", "updated_at", "title", "author", "tags", "content"]

            key_list = data.keys()

            for item in key_list:
                if item in allowed_list_keys:
                
                    output = Post.update_publication(product_id, data)
                    output.pop("_id")
                    return output, HTTPStatus.OK

        return {"error": "Requested resource does not exist."}, HTTPStatus.NOT_FOUND
    except AttributeError:
        return {"error": "Requested resource does not exist."}, HTTPStatus.NOT_FOUND


def delete_one_publication(product_id):

    output = Post.delete_publication(product_id)

    if output:
        output.pop("_id")
        return {"deleted": output}, HTTPStatus.OK

    return {"error": "Requested resource does not exist."}, HTTPStatus.NOT_FOUND
    



