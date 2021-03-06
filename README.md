# Django-Rest-API-Assighnment

# Overview:

Django REST framework is a powerful and flexible toolkit for building Web APIs.
In this Repo i worked on Django Rest Api Assighnemnets.

# Questions: 
    a. Create a database (use sqlite3 database if using Python or any local DB) containing two tables Books and Authors. 
    Add appropriate columns to the tables. Every bookhas a single author and referential integrity should be maintained.
  
    b. Create a Rest API which supports the following operations:
      - Insert, update and select on Books.
      - Handle exception for adding Authors who are not present in the able.

    c. Please follow industry standards while writing the code and include basic schema and data validations.

    d. Use one of the following languages:
      - Python.
      - Java/dotnetiii.
      - NodeJS.
  
  
# Requirements

* Python (3.8)
* Django (3.1)
* Postman/Browser to PUT and GET Data
* Sqlite3

# Installation
  Firist you need to clone this repo then

  Install `requirement.txt` using using bellow specified command
      `python3 requiement.txt`
      "This will install the Django Framework and reqired nessecary libraries including Rest Framework"

  after installing you can directly run 'python3 manage.py run server' to intilize this repo

**Output**: *Screenshot from the browsable API*

# Output Screenshots 
**(Note: local host may change based on that you have to specify local host port number)**

* To get the admin Panal  we need to pass `http://127.0.0.1:8000/admin/` in Browser it appears as below image

![alt text](https://github.com/NikhilG50/Django-Rest-API-Assighnment/blob/main/Output_Screenshots/adminPanal_view.png)



* To get the AuthourList we need to pass `http://127.0.0.1:8000/author/` in Browser it appears as below image

![alt text](https://github.com/NikhilG50/Django-Rest-API-Assighnment/blob/main/Output_Screenshots/AuthourList.png)



* To get BookList we need to pass `http://127.0.0.1:8000/author/` in Browser it appears as below image

![alt text](https://github.com/NikhilG50/Django-Rest-API-Assighnment/blob/main/Output_Screenshots/BookList.png)



*To get Specific author detail  we need to pass  `http://127.0.0.1:8000/author_detail/3/` in Browser it appears as below image

![alt text](https://github.com/NikhilG50/Django-Rest-API-Assighnment/blob/main/Output_Screenshots/AuthorDetail_3rd.png)



* To get Specific Book Detail we we need to pass  `http://127.0.0.1:8000/book_detail/1/` in Browser it appears as below image
 
![alt text](https://github.com/NikhilG50/Django-Rest-API-Assighnment/blob/main/Output_Screenshots/BookDetail_1.png)



## Thank You
