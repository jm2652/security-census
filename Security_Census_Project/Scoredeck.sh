#!/bin/bash

# scoredeck.sh
# Collect scorecard data from a set of repos listed in repos.txt
# and store in files inside a data folder
#
# Usage:
# $ ./scoredeck.sh
#
# Requires GITHUB_AUTH_TOKEN to be set to a valid GitHub personal access
# token.
#
# $ export GITHUB_AUTH_TOKEN=fldkjfldkjflkdjflkjdlkfjdkl
#
# Input data comes from a file named repos.txt
# Each repo is stored on a separate line
# The last line in the file should be empty
#
# Output data for each repo is stored in a separate, individual json file.

# export GITHUB_AUTH_TOKEN=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

echo "Scoredeck script is running."
echo ""

# a loop through the repos listed in repos.txt
while read name
do
  # remove slashes from github repo name to make naming files without
  # errors possible
  output_filename=$(echo $name | sed 's#/#-#g')
  echo "Scanning ${name}"
  # read in GitHub personal access token set in environment variable
  GITHUB_AUTH_TOKEN=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
  # GITHUB_AUTH_TOKEN=${GITHUB_AUTH_TOKEN:-default} \
    scorecard --repo="$name" \
    --format="json" > "data/${output_filename}.json" # output json to a file
done < ~/Desktop/Coding/new_repos.txt # read in repos.txt file line-by-line

echo ""
echo "Scoredeck script has completed."
echo ""