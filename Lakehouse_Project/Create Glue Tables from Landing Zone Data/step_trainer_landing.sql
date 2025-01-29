CREATE EXTERNAL TABLE `stedi.step_trainer_landing` (
    `sensor_reading_time` TIMESTAMP COMMENT 'from deserializer',
    `serial_number` STRING COMMENT 'from deserializer',
    `distance_from_object` DOUBLE COMMENT 'from deserializer'
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
    'paths'='sensor_reading_time,serial_number,distance_from_object'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://step_trainer--bucket/step_trainer_landing/'
TBLPROPERTIES (
    'classification'='json',
    'typeOfData'='file'
);