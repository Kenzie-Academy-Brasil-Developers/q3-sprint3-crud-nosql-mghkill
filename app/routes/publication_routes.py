from flask import Flask
from app.controllers import publication_controller



def all_routes(app: Flask):

    @app.post('/create_post')
    def register_publication():
        return publication_controller.register_one_publication()



    @app.get("/read_post_by_id/<int:product_id>")
    def publication_by_id(product_id):
        return publication_controller.filter_publication(product_id)
    
    
    
    @app.get('/read_posts')
    def all_publication():
        return publication_controller.get_all_publication()


    
    @app.patch('/update_post/<int:product_id>')
    def update_publication(product_id):
        return publication_controller.update_one_publication(product_id)

    

    @app.delete('/delete_post/<int:product_id>')
    def delete_publication(product_id):
        return publication_controller.delete_one_publication(product_id)
        

