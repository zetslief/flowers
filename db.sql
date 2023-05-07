CREATE TABLE flower (
  	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	image_url TEXT
);

CREATE TABLE "user" (
  	id SERIAL PRIMARY KEY,
  	first_name VARCHAR(100) NOT NULL,
  	last_name VARCHAR(100) NOT NULL,
  	email VARCHAR(100) NOT NULL UNIQUE,
	phone VARCHAR(20),
	address VARCHAR(100) NOT NULL
);

CREATE TABLE "order" (
  	id SERIAL PRIMARY KEY,
  	user_id INTEGER REFERENCES "user"(id),
  	flower_id INTEGER REFERENCES flower(id),
  	quantity INTEGER NOT NULL,
	order_date TIMESTAMP NOT NULL
);

