import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node step_landing
step_landing_node1738033694105 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_trusted", transformation_ctx="step_landing_node1738033694105")

# Script generated for node accelerometer_landing
accelerometer_landing_node1738033715436 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_trusted", transformation_ctx="accelerometer_landing_node1738033715436")

# Script generated for node Join
Join_node1738033760953 = Join.apply(frame1=step_landing_node1738033694105, frame2=accelerometer_landing_node1738033715436, keys1=["sensorreadingtime"], keys2=["timestamp"], transformation_ctx="Join_node1738033760953")

# Script generated for node SQL Query
SqlQuery946 = '''
select count(*) from myDataSource

'''
SQLQuery_node1738033877055 = sparkSqlQuery(glueContext, query = SqlQuery946, mapping = {"myDataSource":Join_node1738033760953}, transformation_ctx = "SQLQuery_node1738033877055")

# Script generated for node machine_learning_curated
EvaluateDataQuality().process_rows(frame=SQLQuery_node1738033877055, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1738033690947", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
machine_learning_curated_node1738034001773 = glueContext.getSink(path="s3://step-trainer--bucket/machine_learning_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="machine_learning_curated_node1738034001773")
machine_learning_curated_node1738034001773.setCatalogInfo(catalogDatabase="stedi",catalogTableName="machine_learning_curated")
machine_learning_curated_node1738034001773.setFormat("glueparquet", compression="snappy")
machine_learning_curated_node1738034001773.writeFrame(SQLQuery_node1738033877055)
job.commit()