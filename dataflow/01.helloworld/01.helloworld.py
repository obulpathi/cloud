import logging

# import beam
import apache_beam as beam


# set up logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# Create a pipeline executing on a direct runner (local, non-cloud).
p = beam.Pipeline('DirectPipelineRunner')

# Create a PCollection with names and write it to a file.
(p
 | beam.io.Read(beam.io.TextFileSource('./input/tensorflow.txt'))
 | beam.Write(beam.io.TextFileSink('./output/names')))

# Execute the pipeline.
p.run()
