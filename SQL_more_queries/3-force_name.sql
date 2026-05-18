-- Creates the table force_name on your MySQL server where the name cannot be null.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
