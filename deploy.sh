gcloud auth login

gcloud config set project agentone-466906

export GOOGLE_CLOUD_PROJECT="agentone-466906"

export GOOGLE_CLOUD_LOCATION="us-central1"

export AGENT_PATH="sahayak"

export SERVICE_NAME="sahayak "

export APP_NAME="sahayak "

uv run adk deploy cloud_run --project=$GOOGLE_CLOUD_PROJECT --region=$GOOGLE_CLOUD_LOCATION --service_name=$SERVICE_NAME --app_name=$APP_NAME --with_ui $AGENT_PATH
