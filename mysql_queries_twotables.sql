CREATE TABLE ORIGINAL_FILE(
  user_id  INT UNSIGNED NOT NULL AUTO_INCREMENT,
  original_file_name VARCHAR(50) NOT NULL,
  unique_file_name VARCHAR(40) NOT NULL,

  PRIMARY KEY(user_id),

  CONSTRAINT uniq_dbfilename UNIQUE (unique_file_name)
);


CREATE TABLE ANALYSES(
  user_id  INT UNSIGNED NOT NULL AUTO_INCREMENT,
  unique_file_name_1 VARCHAR(50) NOT NULL,
  unique_file_name_2 VARCHAR(40) NOT NULL,
  analysis_type VARCHAR(40) NOT NULL,
  output_file_name VARCHAR(40) NOT NULL,

  PRIMARY KEY(user_id),

  CONSTRAINT uniq_dboutfilename UNIQUE (output_file_name)
);
