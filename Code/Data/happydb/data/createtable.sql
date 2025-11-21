DROP TABLE IF EXISTS hm_data;
DROP TABLE IF EXISTS writers_data;

CREATE TABLE writers_data (
    wid int PRIMARY KEY,
    age text,
    country text,
    gender text,
    marriage text,
    parenthood boolean
);

CREATE TABLE hm_data (
    hm_id int PRIMARY KEY,
    wid int,
    reflection_period text,
    hm text,
    num_sentences int,
    hm_category text
);

