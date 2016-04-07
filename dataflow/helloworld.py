# Standard imports
import google.cloud.dataflow as df

# Create a pipeline executing on a direct runner (local, non-cloud).
p = df.Pipeline('DirectPipelineRunner')

# Create a PCollection with names and write it to a file.
(p
 | df.Create('add names', ['Ann', 'Joe'])
 | df.Write('save', df.io.TextFileSink('./names')))

# Execute the pipeline.
p.run()
