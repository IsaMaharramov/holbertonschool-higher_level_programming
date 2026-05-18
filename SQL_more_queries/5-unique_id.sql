-- Creates the table unique_id with a default ID value of 1 that must be unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
