CREATE TABLE users (
	id          		serial,
	mail        		varchar(256)    	NOT NULL,
	password    		varchar(64)     		NOT NULL,
	solt        		varchar(32)     		NOT NULL,
	name        		varchar(64)     		NOT NULL,
	is_newuser  		boolean         		NOT NULL,
	user_type   		smallint        		NOT NULL,
	created_at  		timestamp       	NOT NULL,
	updated_at  		timestamp       	NOT NULL,
	PRIMARY KEY (id)
);


CREATE TABLE departments (
id      			smallserial,
name    		varchar(30)     	NOT NULL,
PRIMARY KEY (id)
);


CREATE TABLE students (
id              		 serial,
graduation_year	 smallint 	NOT NULL,
student_number  	 integer 	NOT NULL,
department_id       	 smallint,
teacher_id      		 integer,
PRIMARY KEY (id),
FOREIGN KEY (id) 	REFERENCES users(id),
FOREIGN KEY (department_id) 	REFERENCES departments(id),
FOREIGN KEY (teacher_id) 		REFERENCES users(id)
);


CREATE TABLE change_passwords (
id          		smallserial,
user_id     		integer     	NOT NULL,
hash        		varchar(64) 	NOT NULL,
is_changed  		boolean     	NOT NULL    DEFAULT false,
exp_datetime 		timestamp	 NOT NULL,
created_at  		timestamp   	NOT NULL
DEFAULT CURRENT_TIMESTAMP ,
updated_at  		timestamp   	 NOT NULL
DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (user_id) 	REFERENCES users(id)
);


CREATE TABLE web_push (
 	id          		serial,
user_id     		integer         		NOT NULL,
public_key  		varchar(255)   		NOT NULL,
endpoint    		varchar(2048)   	NOT NULL,
secret_key  		varchar(255)    	NOT NULL,
PRIMARY KEY (id),
	FOREIGN KEY (user_id)	REFERENCES users(id)
);


CREATE TABLE industries (
id 			smallserial,
name 			varchar(64) 	NOT NULL,
is_show 		boolean 	NOT NULL DEFAULT true,
PRIMARY KEY (id)
);


CREATE TABLE occupations (
id          		smallserial,
name        		varchar(64)     	NOT NULL,
is_show     		boolean         	NOT NULL DEFAULT true,
industry_id 		smallint 	NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (industry_id)		REFERENCES industries(id)
);


CREATE TABLE reports (
	id 			serial,
	student_id 		integer 		NOT NULL,
	teacher_id 		integer 		NOT NULL,
	company 		varchar(256) 		NOT NULL,
	zip_code 		varchar(7) 		NOT NULL,
	prefecture 		varchar(4) 		NOT NULL,
	address 		varchar(256) 		NOT NULL,
	occupations_id 	smallint 		NOT NULL,
	form 			smallint 		NOT NULL,
	advice 			varchar(1024),
	is_show 		boolean 		NOT NULL DEFAULT true,
	job_teacher_id 	integer  		NOT NULL,
	test_result 		smallint 		NOT NULL,
	created_at 		timestamp 		NOT NULL,
	updated_at 		timestamp 		NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (student_id) REFERENCES users(id),
	FOREIGN KEY (teacher_id) REFERENCES users(id),
	FOREIGN KEY (job_teacher_id) REFERENCES users(id),
	FOREIGN KEY (occupations_id) REFERENCES occupations(id)
);

CREATE TABLE tests (
	id 			serial,
	report_id 	  	integer,
	stage 		 	smallint 		NOT NULL,
	start_date 		timestamp 		NOT NULL,
	end_date 		timestamp 		NOT NULL,
	datails_text 		varchar(1024),
	is_status 		smallint 		NOT NULL,
	is_checked_student 	boolean 		NOT NULL,
	created_at 		timestamp 		NOT NULL
DEFAULT CURRENT_TIMESTAMP,
	updated_at 		timestamp 		NOT NULL
DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (report_id)	REFERENCES reports(id)
);


CREATE TABLE test_details(
	test_id			 integer,
	detail_id 		smallint,
	test_category 		smallint 	NOT NULL,
data1 			varchar(32),
	data2 			varchar(32),
	created_at 		timestamp 	NOT NULL
DEFAULT CURRENT_TIMESTAMP,
	updated_at 		timestamp 	NOT NULL
DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (test_id,detail_id),
	FOREIGN KEY (test_id) REFERENCES tests(id)
);

CREATE TABLE test_report_reviews (
	review_id	 	serial,
	test_id		 	integer,
	comment 		varchar(1024)	 	NOT NULL,
	created_at	 	timestamp	 	NOT NULL,
	updated_at	 	timestamp	 	NOT NULL,
	PRIMARY KEY (review_id,test_id),
	FOREIGN KEY (test_id) REFERENCES tests(id)
);