-- Creamos el esquema de trabajo
create schema datawitches authorization vezgldfh;

-- Creamos la tabla airbnb
create table datawitches.airbnb (
	"ID" integer NOT NULL, -- PK
	"Host ID" integer NULL,
	"Host Since" date NULL,
	"Neighbourhood" varchar(200) NULL,
	"City" varchar(50) NULL,
	"State" varchar(50) NULL,
	"Zipcode" integer NULL,
	"Latitude" varchar(100) NULL,
	"Longitude" varchar(100) NULL,
	"Property Type" varchar(50) NULL,
	"Room Type" varchar(50) NULL,
	"Bathrooms" integer NULL,
	"Bedrooms" integer NULL,
	"Beds" integer NULL,
	"Bed Type" varchar(100) NULL,
	"Square Feet" float NULL,
	"Cleaning Fee" float NULL,
	"Availability 365" integer NULL,
	"Review Scores Location" float NULL,
	"Cancellation Policy" varchar(50) NULL,
	"Accommodates" integer NULL,
	"Reviews per Month" float NULL,
	"Minimum Nights" integer NULL,
	"Price" float NULL,
	"Weekly Price" float NULL,
	"Monthly Price" float NULL,
	"Occupancy" float NULL
);

-- Añadimos la PK
alter table datawitches.airbnb 
add constraint airbnb_PK primary key ("ID");


-- Creamos la tabla amenities
create table datawitches.amenities (
	"ID" integer NOT NULL, -- PK, FK
	"Self Check-In" boolean,
	"Smartlock" boolean,
	"Air conditioning" boolean,
	"Elevator" boolean,
	"Essentials" boolean,
	"Internet" boolean,
	"Heating" boolean,
	"Pets allowed" boolean,
	"Smoking allowed" boolean,
	"Pool" boolean,
	"TV" boolean,
	"Kitchen" boolean,
	"Gym" boolean
);

--- Añadimos la PK y la FK
alter table datawitches.amenities
add constraint amenities_PK primary key ("ID");

alter table datawitches.amenities
add constraint amenities_airbnb_FK foreign key("ID")
references datawitches.airbnb("ID");
