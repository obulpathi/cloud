Cloud TensorFlow:

- Setup process: https://cloud.google.com/ml/docs/how-tos/getting-set-up
- Quickstart: https://cloud.google.com/ml/docs/quickstarts/training
- git clone git@github.com:GoogleCloudPlatform/cloudml-samples.git

Commands:

- cloud beta ml init-project


JOB_NAME=datalab_ml_mnist_1

PROJECT_ID='thedatalabproject'
TRAIN_BUCKET=gs://datalab-models
TRAIN_PATH=${TRAIN_BUCKET}/${JOB_NAME}
gsutil rm -rf ${TRAIN_PATH}

cloud beta ml jobs submit training ${JOB_NAME} \
  --package-path=trainer \
  --module-name=trainer.task \
  --staging-bucket="${TRAIN_BUCKET}" \
  --region=us-central1 \
  -- \

  --train_dir="${TRAIN_PATH}/train"

cloud beta ml jobs submit training ${JOB_NAME} --package-path=trainer --module-name=trainer.task --staging-bucket=${TRAIN_BUCKET} --region=us-central1  --  --train_dir=${TRAIN_PATH}/train

cloud beta ml jobs describe --project ${PROJECT_ID} ${JOB_NAME}

gsutil ls ${TRAIN_PATH}/train
