CREATE EXTERNAL TABLE `stedi.customer_landing` (
    `customer_id` STRING COMMENT 'from deserializer',
    `email` STRING COMMENT 'from deserializer',
    `registration_date` TIMESTAMP COMMENT 'from deserializer',
    `share_with_research` BOOLEAN COMMENT 'from deserializer'
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
    'paths'='customer_id,email,registration_date,share_with_research'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://customer--bucket/customer_landing/'
TBLPROPERTIES (
    'classification'='json',
    'typeOfData'='file'
);