# use taxi_booking;
#
# CREATE TABLE ADMIN (
#   Admin_id  int(10) NOT NULL AUTO_INCREMENT,
#   Username  varchar(50) NOT NULL,
#   Password  varchar(50) NOT NULL,
#   user_type varchar(50) NOT NULL,
#   PRIMARY KEY (Admin_id));
#
# CREATE TABLE Booking (
#   Booking_id       int(10) NOT NULL AUTO_INCREMENT,
#   PickUp_location  varchar(50) NOT NULL,
#   DropOff_location varchar(50) NOT NULL,
#   PickUp_Time      varchar(10) NOT NULL,
#   PickUp_date      date NOT NULL,
#   DropOff_Time     varchar(50) NOT NULL,
#   DropOff_Date     date NOT NULL,
#   Booking_Status   varchar(50) NOT NULL,
#   driver_id        int(10),
#   customer_id      int(10) NOT NULL,
#   Admin_id         int(10) NOT NULL,
#   PRIMARY KEY (Booking_id));
#
#
# CREATE TABLE Customer (
#   customer_id    int(10) NOT NULL AUTO_INCREMENT,
#   first_name     varchar(255) NOT NULL,
#   last_name      varchar(50) NOT NULL,
#   address        varchar(255) NOT NULL,
#   gender         varchar(255) NOT NULL,
#   email          varchar(255) NOT NULL,
#   phone_num      varchar(50) NOT NULL,
#   user_type      varchar(50) NOT NULL,
#   payment_method varchar(50) NOT NULL,
#   Password       varchar(255) NOT NULL,
#   PRIMARY KEY (customer_id));
#
# CREATE TABLE Driver (
#   driver_id     int(10) NOT NULL AUTO_INCREMENT,
#   First_Name    varchar(50) NOT NULL,
#   last_name     varchar(50) NOT NULL,
#   Address       varchar(50) NOT NULL,
#   Phone_num     varchar(50) NOT NULL,
#   email         varchar(50) NOT NULL,
#   License_plate varchar(50) NOT NULL,
#   Password      varchar(50) NOT NULL,
#   user_type     varchar(50) NOT NULL,
#   PRIMARY KEY (driver_id));
#
# ALTER TABLE Booking ADD CONSTRAINT FKBooking64193 FOREIGN KEY (driver_id) REFERENCES Driver (driver_id);
# ALTER TABLE Booking ADD CONSTRAINT FKBooking472595 FOREIGN KEY (Admin_id) REFERENCES ADMIN (Admin_id);
# ALTER TABLE Booking ADD CONSTRAINT do FOREIGN KEY (customer_id) REFERENCES Customer (customer_id);
#
#
# ALTER TABLE Booking DROP FOREIGN KEY FKBooking64193;
# ALTER TABLE Booking DROP FOREIGN KEY FKBooking472595;
# ALTER TABLE Booking DROP FOREIGN KEY do;
# DROP TABLE IF EXISTS ADMIN;
# DROP TABLE IF EXISTS Booking;
# DROP TABLE IF EXISTS Customer;
# DROP TABLE IF EXISTS Driver;
