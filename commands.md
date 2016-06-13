Basic example:
mvn compile exec:java \
    -Dexec.mainClass=com.example.WordCount \
    -Dexec.args="--project=thedataclouds \
    --stagingLocation=gs://wordcount76374623/staging/ \
    --output=gs://wordcount76374623/output \
    --runner=BlockingDataflowPipelineRunner"


Word count debug:
mvn compile exec:java \
  -Dexec.mainClass=com.google.cloud.dataflow.examples.DebuggingWordCount \
  -Dexec.args="--project=thedataclouds \
    --stagingLocation=gs://wordcount76374623/staging-debug/ \
    --runner=BlockingDataflowPipelineRunner \
    --output=gs://wordcount76374623/output-debug"
