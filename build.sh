#!/usr/bin/env bash
# Rebuild dist/github-star-magnet.skill (a .skill file is a zip of the skill folder).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist
rm -f dist/github-star-magnet.skill
(cd skill && zip -rq ../dist/github-star-magnet.skill github-star-magnet -x '*/__pycache__/*' '*.pyc')
echo "Built dist/github-star-magnet.skill"
