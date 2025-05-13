-- Java_MSA.lsb.Users definition

-- Drop table

-- DROP TABLE Java_MSA.lsb.Users;

CREATE TABLE Java_MSA.lsb.Users (
    id INT IDENTITY(1,1) NOT NULL,
    username NVARCHAR(50),
    email NVARCHAR(100),
    hashed_password NVARCHAR(255),
    created_at DATETIME2 DEFAULT GETDATE() NULL,
    updated_at DATETIME2 DEFAULT GETDATE() NULL,
    PRIMARY KEY (id)
);
-- Add a unique constraint to the username and email columns
ALTER TABLE Java_MSA.lsb.Users