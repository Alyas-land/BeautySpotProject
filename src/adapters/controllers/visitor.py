from flask import render_template, request

class VisitorController:
    def __init__(self) -> None:
        pass

    def main(self):
        return render_template('/main/index.html', current_page='main')
    
    def product_us(self):
        return render_template('/main/product-us.html', current_page='product_us')
        
    def about(self):
        return render_template('/main/about.html', current_page='about')
    
    def contact(self):
        return render_template('/main/contact.html') 
        