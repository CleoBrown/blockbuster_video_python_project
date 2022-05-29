# Blockbuster project
## Steps to run
1. **Create the database**

Run:<br>

(The below command must be run first to ensure the database tables are created and the primary keys are reset to 1. The database primary keys are set to match the picture file names).
```
sqlite3 db/product_manager.db < db/product_manager.sql
```

2. **Insert data from console.py file**

Run:<br>
```
python console.py
```

3. **Run the app on localhost:5000**

Run:<br>
```
flask run
```