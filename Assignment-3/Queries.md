# DB queries for the following 
1. Query to create the user table 
2. Query to create the events table 
3. Query to insert into User table 
4. Query to insert into Events table 
5. Query to get all events for today   
    -> Both Yearly and OneTime (For one time, ongoing events should come)  
6. Query to get all users for a list of uid   
    (Eg. get users whose uid is one of (1, 2, 6, 8, 9)) 
7. Query to get all events for a uid (Eg. get all events for uid=1) 
8. Query to get all events for the next 7 days.

## Create schema
```sql
CREATE DATABASE  user_events;
USE user_events;
```
## Create a function to generate uid(Random unique id)
```sql
DELIMITER $$
CREATE FUNCTION uuid4()
    RETURNS CHAR(36) NO SQL
BEGIN
    -- 1th and 2nd block are made of 6 random bytes
    SET @h1 = HEX(RANDOM_BYTES(4));
    SET @h2 = HEX(RANDOM_BYTES(2));

    -- 3th block will start with a 4 indicating the version, remaining is random
    SET @h3 = SUBSTR(HEX(RANDOM_BYTES(2)), 2, 3);

    -- 4th block first nibble can only be 8, 9 A or B, remaining is random
    SET @h4 = CONCAT(HEX(FLOOR(ASCII(RANDOM_BYTES(1)) / 64)+8),
                SUBSTR(HEX(RANDOM_BYTES(2)), 2, 3));

    -- 5th block is made of 6 random bytes
    SET @h5 = HEX(RANDOM_BYTES(6));

    -- Build the complete UUID
    RETURN LOWER(CONCAT(
        @h1, '-', @h2, '-4', @h3, '-', @h4, '-', @h5
    ));
END $$
DELIMITER ;
```

## 1. Query to create the user table 
```sql
CREATE TABLE tbl_user_info(
uid VARCHAR(36) PRIMARY KEY,
name VARCHAR(50) NOT NULL,
gender ENUM('Male', 'Female'),
email VARCHAR(255) UNIQUE KEY NOT NULL
);
```
## 2. Query to create the event table
```sql
CREATE TABLE tbl_event(
id INT NOT NULL AUTO_INCREMENT,
uid VARCHAR(36) NOT NULL,
name VARCHAR(50),
occurance ENUM('ONETIME', 'YEARLY'),
startDate DATE NOT NULL,
endDate DATE,
PRIMARY KEY(id),
FOREIGN KEY (uid) REFERENCES tbl_user_info(uid)
);
```
## 3. Query to insert into User table
```sql
INSERT INTO tbl_user_info (uid, name, gender, email) VALUES
(uuid4(), 'Pawan Kumar', 'Male', 'pawankumar@gmail.com'),
(uuid4(), 'Avichal Gupta', 'Male', 'avichalgupta@gmail.com'),
(uuid4(), 'Harshit Gupta', 'Male', 'harshitgupta@gmail.com'),
(uuid4(), 'Priya Singh', 'Female', 'priyasingh@gmail.com'),
(uuid4(), 'Ritik Kumar', 'Male', 'ritikkumar@gmail.com'),
(uuid4(), 'Abhinav Singh', 'Male', 'abhinavsingh@gmail.com'),
(uuid4(), 'Shalini Singh', 'Female', 'shalinisingh'),
(uuid4(), 'Abhay Singh', 'Male', 'abhaysingh@gmail.com'),
(uuid4(),'Yash Sagar', 'Male', 'yashsager@gmail.com'),
(uuid4(), 'Abhishek Gupta', 'Male', 'abhishekgupta@gmail.com');
```
## 4. Query to insert into Events table
```sql
-- 4.1 without endDate
INSERT INTO tbl_event (uid, name, occurance, startDate) VALUES
('27d43029-19c6-4eef-b482-5fed330c1815', 'Quiz', 'ONETIME', '2022-01-21'),
('27d43029-19c6-4eef-b482-5fed330c1815', 'Webinar', 'ONETIME', '2022-01-26'),
('27d43029-19c6-4eef-b482-5fed330c1815', "Pawan's Birthday", 'YEARLY', '2000-01-22'),
('01a839b1-0bcb-4255-8dd3-f9556719e240', "Yash's Birthday", 'YEARLY', '2000-01-21'),
('ffb3aa58-aaaa-4b52-8a46-a579359b4a67', "Harsit's Birthday", 'YEARLY', '2000-01-27'),
('30a7dc01-023d-41c1-af7b-cc2f112011d2', 'Medical Appointment', 'ONETIME', '2022-01-21'),
('27d43029-19c6-4eef-b482-5fed330c1815', 'Medical Appointment', 'YEARLY', '2022-01-23'),
('27d43029-19c6-4eef-b482-5fed330c1815', 'JEE ADVANCE PAPER', 'ONETIME', '2022-05-25'),
('0a7a79c0-2ce0-4646-b8fc-13af440a6cfe', 'Visit to Taj Mahal', 'YEARLY', '2022-01-21')
;

-- 4.2 with enddate
INSERT INTO tbl_event (uid, name, occurance, startDate, endDate) VALUES
('01a839b1-0bcb-4255-8dd3-f9556719e240', 'Examination', 'ONETIME', '2022-01-27', '2022-02-03'),
('e258a6ac-0a83-4c20-966e-307652d7a8db', 'Examination', 'ONETIME', '2022-01-27', '2022-02-03'),
('df51737b-bbab-4812-bc81-9e5e0e00b3b9', 'Examination', 'ONETIME', '2022-01-27', '2022-02-03'),
('7cf6e1ae-42e8-48d9-b173-a20d02cae81b', 'Marriage', 'ONETIME', '2022-01-23', '2022-01-26'),
('ee230231-2c59-4f0b-bead-88c549d1e906', 'Singapure Tour', 'ONETIME', '2022-04-10', '2022-04-20'),
('27d43029-19c6-4eef-b482-5fed330c1815', 'Visit to Village', 'YEARLY', '2022-03-01', '2022-03-7'),
('30a7dc01-023d-41c1-af7b-cc2f112011d2', 'Visit to Home', 'ONETIME', '2022-01-21', '2022-01-27'),
('a70e4bfe-f168-489f-ad16-7fcb1b9acc58', 'Examination', 'ONETIME', '2022-01-27', '2022-02-03'),
('e258a6ac-0a83-4c20-966e-307652d7a8db', 'Examination', 'ONETIME', '2022-01-27', '2022-02-03'),
('7cf6e1ae-42e8-48d9-b173-a20d02cae81b', 'Visit to Manali', 'ONETIME', '2022-02-15', '2022-02-16'),
('a70e4bfe-f168-489f-ad16-7fcb1b9acc58', 'Singapure Tour', 'ONETIME', '2022-04-10', '2022-04-20')
;
```
## 5. Query to get all events for today 
```sql
SELECT * FROM tbl_event
WHERE (  tbl_event.startDate = CURDATE()
          OR
			( tbl_event.occurance = 'ONETIME'
			AND ( 
				  (  
                      tbl_event.endDate = NULL 
                         AND tbl_event.startDate = CURDATE() 
                  )
                  
				 OR 
				  (
					tbl_event.endDate != NULL
						AND
							(tbl_event.startDate <= CURDATE() AND tbl_event.endDate >= CURDATE())
				   )
				)
		)
		OR
		( tbl_event.occurance = 'YEARLY'
			AND ( 
				  (  
                      tbl_event.endDate IS NULL 
                         AND DATE_FORMAT(tbl_event.startDate, '%m%d') = DATE_FORMAT(CURDATE(), '%m%d')
                  )
                  
				 OR 
				  (
					tbl_event.endDate IS NOT NULL
						AND
                            ( DATE_FORMAT(tbl_event.startDate, '%m%d') <= DATE_FORMAT(CURDATE(), '%m%d') 
                                AND DATE_FORMAT(tbl_event.endDate, '%m%d') >= DATE_FORMAT(CURDATE(), '%m%d')
                                
							)
				   )
				)
		)
	  );
```
     
## 6. Query to get all users for a list of uid
```sql
SELECT *
FROM tbl_user_info
WHERE tbl_user_info.uid IN ('ffb3aa58-aaaa-4b52-8a46-a579359b4a67',
							'0a7a79c0-2ce0-4646-b8fc-13af440a6cfe',
							'30a7dc01-023d-41c1-af7b-cc2f112011d2',
							'27d43029-19c6-4eef-b482-5fed330c1815',
							'ee230231-2c59-4f0b-bead-88c549d1e906');
```
    (Eg. get users whose uid is one of (1, 2, 6, 8, 9)) 
## 7. Query to get all events for a uid (Eg. get all events for uid=1)
```
SELECT *
FROM tbl_event
WHERE tbl_event.uid = '27d43029-19c6-4eef-b482-5fed330c1815';
```
## 8. Query to get all events for the next 7 days.
```sql
SELECT *
FROM tbl_event
WHERE (
		tbl_event.startDate BETWEEN  CURDATE()+1 AND CURDATE()+7
        OR (
			 tbl_event.occurance = 'YEARLY' 
             AND ( 
					( DATE_FORMAT(tbl_event.startDate, '%m-%d') BETWEEN
							DATE_FORMAT(CURDATE()+1, '%m-%d') AND DATE_FORMAT(CURDATE()+7, '%m-%d')
					)
                    OR
                    ( DATE_FORMAT(tbl_event.endDate, '%m-%d') BETWEEN
							DATE_FORMAT(CURDATE()+1, '%m-%d') AND DATE_FORMAT(CURDATE()+7, '%m-%d')
					)
                            
					
                            
				 )
                
            )
            
	  );
```

---



