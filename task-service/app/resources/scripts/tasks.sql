-- Java_MSA.lsb.Tasks definition

-- Drop table

-- DROP TABLE Java_MSA.lsb.Tasks;

CREATE TABLE Java_MSA.lsb.Tasks (
	id int IDENTITY(1,1) NOT NULL,
	user_id int NOT NULL,
	title nvarchar(100) ,
	description nvarchar(MAX) NULL,
    created_by nvarchar(50) NULL,
	due_date datetime2 NULL,
	is_completed bit DEFAULT 0 NULL,
	created_at datetime2 DEFAULT getdate() NULL,
    updated_at datetime2 DEFAULT getdate() NULL,
    PRIMARY KEY (id)
);