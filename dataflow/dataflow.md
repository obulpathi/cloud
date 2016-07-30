PROJECT=thedataclouds
BUCKET=gs://mybucket78965

python 01.wordcount.py --output=./output/wordcount

python 01.wordcount.py --output=./output/wordcount \
  --project $PROJECT \
  --job_name $PROJECT-wordcount \
  --runner BlockingDataflowPipelineRunner \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --output $BUCKET/output


python 01.wordcount.py --output=./output/wordcount \
    --project $PROJECT \
    --job_name wordcount \
    --runner DataflowPipelineRunner \
    --staging_location $BUCKET/staging \
    --temp_location $BUCKET/temp \
    --output $BUCKET/output


parser.add_argument('--input', dest='input', default='gs://dataflow-samples/shakespeare/kinglear.txt', help='Input file to process.')
parser.add_argument('--output', dest='output', required=True, help='Output file to write results to.')

python -m apache_beam.examples.wordcount \
  --project $PROJECT \
  --job_name $PROJECT-wordcount \
  --runner BlockingDataflowPipelineRunner \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --output $BUCKET/output



argv=None
parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input', default='gs://dataflow-samples/shakespeare/kinglear.txt', help='Input file to process.')
parser.add_argument('--output', dest='output', required=True, help='Output file to write results to.')
