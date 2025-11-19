set -x
set -e
echo "Attention: Run it from product root folder"
VERSION="1.2.3"
BRANCH="main"
git checkout $BRANCH
# git pull origin $BRANCH
echo "Collecting data from $VERSION as defined in the 'VERSION' constant"
SOURCE="./"
TARGET_UML="./umls/$VERSION"
TARGET_CC_LOGS="./logs/cyclomatic-complexity/$VERSION/"
TARGET_RAW_LOGS="./logs/raw-metrics/$VERSION/"
TARGET_MI_LOGS="./logs/maintenability-index/$VERSION/"
TARGET_HAL_LOGS="./logs/halstead-metrics/$VERSION/"
TARGET_C2F_LOGS="./logs/code2flow/$VERSION/"
TARGET_COV_LOGS="./logs/coverage/$VERSION/"
TARGET_SMELL_LOGS="./logs/code-smells/$VERSION/"
TARGET_MAAT_LOGS="./logs/code-maat/$VERSION/"

rm -rf "./logs"
mkdir -p $TARGET_UML
mkdir -p $TARGET_CC_LOGS
mkdir -p $TARGET_RAW_LOGS
mkdir -p $TARGET_MI_LOGS
mkdir -p $TARGET_HAL_LOGS
mkdir -p $TARGET_C2F_LOGS
mkdir -p $TARGET_COV_LOGS
mkdir -p $TARGET_SMELL_LOGS
mkdir -p $TARGET_MAAT_LOGS

# gets UMLs
pyreverse --project target-folder --verbose --ignore test_*,tests target-folder/ -d $TARGET_UML

# get cyclomatity complexity
radon cc target-folder/ -nc -O "$TARGET_CC_LOGS/target-folder.log"

# gets raw metrics
radon raw target-folder/ --summary -O "$TARGET_RAW_LOGS/target-folder.log"

# gets maintenability index
radon mi target-folder/ -O "$TARGET_MI_LOGS/target-folder.log"

# gets halstead metrics
radon hal target-folder/ -O "$TARGET_HAL_LOGS/target-folder.log"

# get code to flow
code2flow ./target-folder -o "$TARGET_C2F_LOGS/target-folder.gv"

# get test coverage
python -m coverage run --omit="*venv*,*test*" -m pytest
python -m coverage report > "$TARGET_COV_LOGS/coverage.log"
python -m coverage html -d $TARGET_COV_LOGS

# get code smells
# Uncomment to install the library
# pip install ./code_quality_analyzer-0.1-py3-none-any.whl
analyze_code_quality $SOURCE --config ./code_quality_config.yaml --output "$TARGET_SMELL_LOGS/code-smells"

# get SVN metrics
git log --pretty=format:'[%h] %aN %ad %s' --date=short --numstat --after=1990-01-01 > "$TARGET_MAAT_LOGS/logfile.log"
java -jar code-maat-1.0.2-standalone.jar -l "$TARGET_MAAT_LOGS/logfile.log" -c git -o "$TARGET_MAAT_LOGS/code-maat-organizational.log"
java -jar code-maat-1.0.2-standalone.jar -l "$TARGET_MAAT_LOGS/logfile.log" -c git -a summary -o "$TARGET_MAAT_LOGS/code-maat-summary.log"
java -jar code-maat-1.0.2-standalone.jar -l "$TARGET_MAAT_LOGS/logfile.log" -c git -a coupling -o "$TARGET_MAAT_LOGS/code-maat-coupling.log"
java -jar code-maat-1.0.2-standalone.jar -l "$TARGET_MAAT_LOGS/logfile.log" -c git -a age -o "$TARGET_MAAT_LOGS/code-maat-age.log"