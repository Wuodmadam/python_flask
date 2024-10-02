from flask import *
import pymysql
app=Flask(__name__)

@app.route("/")
def Homepage():
    # connect to DB
    connection = pymysql.connect(host='localhost', user='root', password='', database='my_shop')
    sql="SELECT * FROM products WHERE product_category='phones'"
    sql1="SELECT * FROM products WHERE product_category='electronics'"
    sql2="SELECT * FROM products WHERE product_category='Beauty'"
   
    # you need to have a cursor
    # cursor - is used to run/execute the above SQL
    cursor=connection.cursor()
    cursor1=connection.cursor()
    cursor2=connection.cursor()
    
    # execute
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    


    # fetch all phones rows
    phones=cursor.fetchall()
    electronics=cursor1.fetchall()
    Beauty=cursor2.fetchall()
    
   


    # fetch all electronics rows
   
    return render_template("index.html", phones=phones, electronics=electronics, Beauty=Beauty, )

  

    

# route for single item
@app.route("/single/<products_id>")
def singleitem(products_id):
    connection = pymysql.connect(host='localhost', user='root', password='', database='my_shop')
    sql = "SELECT * FROM products where products_id = %s"
    cursor=connection.cursor()
    cursor.execute(sql,products_id)
    product = cursor.fetchone()
    return render_template("single.html" , product = product)
   
    
@app.route("/about")
def about():
    return "this is my about page"

@app.route("/register")
def register():
    return "this is my registration page"


@app.route("/login")
def login():
    return "this is my  login page"

@app.route("/logout")
def logout():
    return "this is my  logout page"

if __name__== "__main__":
    app.run(debug=True,port=4000)