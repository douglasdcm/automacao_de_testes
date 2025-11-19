#!/bin/bash
set -x
set -e
echo "Attention: Run it from project root folder"
# Define a list of items
branches=("123qwerty" "qwerty321" )

rm -rf "./logs"

# Iterate through the list using a for loop
for branch in "${branches[@]}"; do
  echo "I like to eat $branch."
  VERSION=$branch
  BRANCH=$branch

  git checkout $BRANCH
  echo "Collecting data from $VERSION as defined in the 'VERSION' constant"
  TARGET_RAW_LOGS="./logs/raw-metrics/$VERSION/"
  TARGET_HAL_LOGS="./logs/halstead-metrics/$VERSION/"

  mkdir -p $TARGET_RAW_LOGS
  mkdir -p $TARGET_HAL_LOGS

  # gets raw metrics
  radon raw target_folder/ --summary -O "$TARGET_RAW_LOGS/target_folder.log"

  # gets halstead metrics
  radon hal target_folder/ -O "$TARGET_HAL_LOGS/target_folder.log"
done

