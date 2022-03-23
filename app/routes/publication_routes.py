from flask import Flask
from app.controllers import publication_controller



def all_routes(app: Flask):

    @app.post('/posts')
    def create_post():
        return publication_controller.register_one_publication()



    @app.get("/posts/<int:product_id>")
    def read_post_by_id(product_id):
        return publication_controller.filter_publication(product_id)
    
    
    
    @app.get('/posts')
    def read_posts():
        return publication_controller.get_all_publication()


    
    @app.patch('/posts/<int:product_id>')
    def update_post(product_id):
        return publication_controller.update_one_publication(product_id)

    

    @app.delete('/posts/<int:product_id>')
    def delete_post(product_id):
        return publication_controller.delete_one_publication(product_id)
        

