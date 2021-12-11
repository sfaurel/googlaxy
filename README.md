# Primera parte
para ejecutar la primera parte
~~~ bash
cd <project_path>
python3 googlaxy.py <input_filename> <output_filename>
#or
python3 googlaxy.py <input_full_path> <output_full_path>
~~~
# Segunda parte
~~~ bash
#install Django
pip install Django
cd <project_path>/googlaxy
# clear database
python manage.py flush  
# run server
python manage.py runserver 8000
~~~
## navegacion
acceder a la url 127.0.0.1:8000/currency
funciona igual que la entrada original del programa
la url 127.0.0.1:8000/currency/settings
permite administrar la base de datos
127.0.0.1:8000/currency/settings/items
administra items
127.0.0.1:8000/currency/settings/numerals
administra numerals