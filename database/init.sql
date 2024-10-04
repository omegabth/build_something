-- Create the contacts table
CREATE TABLE contacts (
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    date_of_birth DATE NOT NULL
);

-- Load data from the CSV file into the contacts table
COPY contacts
FROM '/docker-entrypoint-initdb.d/contacts_data.csv' 
DELIMITER ',' 
CSV HEADER;
