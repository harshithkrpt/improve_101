#!/bin/bash
set -e

REGION="ap-south-1"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

API_REPO="todo-api"
UI_REPO="todo-ui"

API_IMAGE="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$API_REPO"
UI_IMAGE="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$UI_REPO"

TAG=$(date +%s)

echo "Logging into ECR..."
aws ecr get-login-password --region $REGION \
| docker login --username AWS --password-stdin \
$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

echo "Ensuring repos exist..."

aws ecr describe-repositories --repository-names $API_REPO --region $REGION >/dev/null 2>&1 \
|| aws ecr create-repository --repository-name $API_REPO --region $REGION

aws ecr describe-repositories --repository-names $UI_REPO --region $REGION >/dev/null 2>&1 \
|| aws ecr create-repository --repository-name $UI_REPO --region $REGION


echo "Building API image..."
docker build -t $API_REPO ./todo
docker tag $API_REPO:latest $API_IMAGE:$TAG

echo "Building UI image..."
docker build -t $UI_REPO ./todo-ui
docker tag $UI_REPO:latest $UI_IMAGE:$TAG


echo "Pushing API..."
docker push $API_IMAGE:$TAG

echo "Pushing UI..."
docker push $UI_IMAGE:$TAG


echo "Done."
echo "API Image: $API_IMAGE:$TAG"
echo "UI Image:  $UI_IMAGE:$TAG"