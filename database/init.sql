CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC(10,2),
    stock INTEGER
);

INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop', 800, 10),
('Mouse', 20, 50),
('Teclado', 35, 30),
('Monitor', 250, 15),
('USB', 10, 100);