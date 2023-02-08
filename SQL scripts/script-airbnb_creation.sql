-- Creo el esquema de trabajo
create schema datawitches authorization vezgldfh;

-- Creo la tabla airbnb
create table datawitches.airbnb (
	"ID" integer NOT NULL,
	"Host ID" integer NULL,
	"Host Since" date NULL,
	"Host Listings Count" integer NULL,
	"Street" varchar(200) NULL,
	"Neighbourhood" varchar(200) NULL,
	"Neighbourhood Cleansed" varchar(200) NULL,
	"Neighbourhood Group Cleansed" varchar(200) NULL,
	"City" varchar(50) NULL,
	"State" varchar(50) NULL,
	"Zipcode" integer NULL,
	"Market" varchar(50) NULL,
	"Latitude" varchar(100) NULL,
	"Longitude" varchar(100) NULL,
	"Property Type" varchar(50) NULL,
	"Room Type" varchar(50) NULL,
	"Accommodates" integer NULL,
	"Bathrooms" integer NULL,
	"Bedrooms" integer NULL,
	"Beds" integer NULL,
	"Bed Type" varchar(100) NULL,
	"Amenities" varchar(600) NULL,
	"Square Feet" float NULL,
	"Price" float NULL,
	"Weekly Price" float NULL,
	"Monthly Price" float NULL,
	"Security Deposit" float NULL,
	"Cleaning Fee" float NULL,
	"Guests Included" integer NULL,
	"Minimum Nights" integer NULL,
	"Maximum Nights" integer NULL,
	"Availability 30" integer NULL,
	"Availability 60" integer NULL,
	"Availability 90" integer NULL,
	"Availability 365" integer NULL,
	"Number of Reviews" integer NULL,
	"Review Scores Rating" float NULL,
	"Review Scores Accuracy" float NULL,
	"Review Scores Cleanliness" float NULL,
	"Review Scores Checkin" float NULL,
	"Review Scores Communication" float NULL,
	"Review Scores Location" float NULL,
	"Review Scores Value" float NULL,
	"Cancellation Policy" varchar(50) NULL,
	"Calculated host listings count" float NULL,
	"Reviews per Month" float NULL,
	"Geolocation" varchar(100) NULL
);

-- PK
alter table datawitches.airbnb 
add constraint PK primary key ("ID");

select * from datawitches.airbnb;


