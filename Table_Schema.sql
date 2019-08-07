# Create Table for Database
DROP TABLE IF EXISTS Street_Condition;
DROP TABLE IF EXISTS Rush_Hour_Routes;




Create Table Street_Condition(
Cnn integer PRIMARY KEY,
Street character varying(50) NOT NULL,
Street_Maintenance character varying(50) NOT NULL
);




Create Table Rush_Hour_Routes(
Cnn integer PRIMARY KEYX,
Street character varying(50) NOT NULL,
Neighborhood character varying(50) NOT NULL
);
