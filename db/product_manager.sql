DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS production_companies;

CREATE TABLE production_companies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR 
);

CREATE TABLE films (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR,
  year INTEGER,
  director VARCHAR,
  description VARCHAR,
  quantity INTEGER,
  buying_cost INTEGER,
  selling_price INTEGER,
  production_company_id INTEGER NOT NULL,
    FOREIGN KEY (production_company_id)
       REFERENCES production_companies (id) 

);