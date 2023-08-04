---
layout: post
title: Oracle Cloud Infrastructure and Oracle University
---

# Oracle Cloud Infrastructure

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/2ef6b4a0-69b1-40d0-b34f-31d08c12ce22)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/be47c495-d821-400a-82c3-1b447bd7a31f)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/969d21d2-e7c8-4327-b871-5ab4b36f372d)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/dae9c9ca-1e0b-4fa2-a38d-35647f323d2d)

```
CREATE USER StoreSalesDBA IDENTIFIED BY A_1_Der_Full_Password;
GRANT CONNECT, RESOURCE TO StoreSalesDBA;
GRANT CREATE TABLE TO StoreSalesDBA;
GRANT CREATE SEQUENCE TO StoreSalesDBA;
GRANT CREATE VIEW TO StoreSalesDBA;
GRANT CREATE SESSION TO StoreSalesDBA;
GRANT CREATE PROCEDURE TO StoreSalesDBA;
GRANT CREATE MATERIALIZED VIEW TO StoreSalesDBA;
GRANT UNLIMITED TABLESPACE to StoreSalesDBA;
```

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/dd13715f-49f6-4056-8fdf-05e4998db482)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/7bb0b10b-eaad-402b-9439-5eb8917636ab)

# Oracle University

<https://mylearn.oracle.com/>

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/e592e8ea-4d3e-49ac-aa54-50a24bf6f285)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/cb5cd5dd-0459-4519-b094-6e08068d17af)

# Database Management Essentials

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/6d156681-8569-4798-9d58-0e793e2181d9)

```sql
-- Executes in both Oracle and PostgreSQL

-- Drop tables if exists
-- DROP TABLE Enrollment;
-- DROP TABLE Offering;
-- DROP TABLE Student;
-- DROP TABLE Course;
-- DROP TABLE Faculty;

CREATE TABLE Student
( StdNo 	    CHAR(11)    CONSTRAINT StdNoRequired NOT NULL,
  StdFirstName  VARCHAR(50) CONSTRAINT StdFirstNameRequired NOT NULL,
  StdLastName   VARCHAR(50) CONSTRAINT StdLastNameRequired NOT NULL,
  StdCity	    VARCHAR(50) CONSTRAINT StdCityRequired NOT NULL,
  StdState	    CHAR(2)	    CONSTRAINT StdStateRequired NOT NULL,
  StdZip	    CHAR(10)    CONSTRAINT StdZipRequired NOT NULL,
  StdMajor	    CHAR(6),
  StdClass	    CHAR(6),
  StdGPA	    DECIMAL(3,2) DEFAULT 0,	
  CONSTRAINT PKStudent PRIMARY KEY (StdNo),	
  CONSTRAINT ValidGPA CHECK ( StdGPA BETWEEN 0 AND 4 ),
  CONSTRAINT ValidStdClass CHECK (StdClass IN ('FR','SO', 'JR','SR')),
  CONSTRAINT MajorDeclared CHECK 
               ( StdClass IN ('FR','SO') OR StdMajor IS NOT NULL ) );

CREATE TABLE Faculty (
FacNo		CHAR(11),
FacFirstName	VARCHAR(30) CONSTRAINT FacFirstNameRequired NOT NULL,
FacLastName	VARCHAR(30) CONSTRAINT FacLastNameRequired NOT NULL,
FacCity		VARCHAR(30) CONSTRAINT FacCityRequired NOT NULL,
FacState	CHAR(2) CONSTRAINT FacStateRequired NOT NULL,
FacZipCode	CHAR(10) CONSTRAINT FacZipRequired NOT NULL,
FacRank		CHAR(4),
FacHireDate	DATE,
FacSalary	DECIMAL(10,2),
FacSupervisor	CHAR(11),
FacDept		CHAR(6),
CONSTRAINT FacultyPK PRIMARY KEY (FacNo), 
CONSTRAINT SupervisorFK FOREIGN KEY (FacSupervisor) REFERENCES Faculty );

CREATE TABLE Course (
CourseNo	CHAR(6),
CrsDesc		VARCHAR(50) CONSTRAINT CrsDescRequired NOT NULL,
CrsUnits	INTEGER,
CONSTRAINT CoursePK PRIMARY KEY (CourseNo), 
CONSTRAINT UniqueCrsDesc UNIQUE (CrsDesc)  );

CREATE TABLE Offering (
OfferNo INTEGER,
CourseNo CHAR(6) CONSTRAINT OffCourseNoRequired NOT NULL,
OffTerm CHAR(6) CONSTRAINT OffTermRequired NOT NULL,
OffYear INTEGER DEFAULT 2022 CONSTRAINT OffYearRequired NOT NULL,
OffLocation VARCHAR(30),
OffTime VARCHAR(10),
FacNo CHAR(11),
OffDays CHAR(6) DEFAULT 'MW',
CONSTRAINT OfferingPK PRIMARY KEY (OfferNo),
CONSTRAINT CourseFK FOREIGN KEY (CourseNo) REFERENCES Course,
CONSTRAINT FacultyFK FOREIGN KEY (FacNo) REFERENCES Faculty );

CREATE TABLE Enrollment (
OfferNo		INTEGER,
StdNo		CHAR(11),
EnrGrade	DECIMAL(3,2) DEFAULT 0,
CONSTRAINT EnrollmentPK PRIMARY KEY (OfferNo, StdNo),
CONSTRAINT OfferingFK FOREIGN KEY (OfferNo) REFERENCES Offering ON DELETE CASCADE,
CONSTRAINT StudentFK FOREIGN KEY (StdNo) REFERENCES Student ON DELETE CASCADE );
```


![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/d0db8b77-d9b4-4250-822d-b9667f67c26e)


Have to modify INSERT statements for date format: (original in format '15-Apr-2008')

```sql
INSERT INTO Faculty
	(FacNo, FacFirstName, FacLastName, FacCity, FacState,
	 FacDept, FacRank, FacSalary, FacSupervisor, FacHireDate, FacZipCode)
	 VALUES ('543-21-0987','VICTORIA','EMMANUEL','BOTHELL','WA','MS','PROF',120000.00,NULL,'2008-04-15','98011-2242');
```
