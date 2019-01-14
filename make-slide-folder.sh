#!/usr/bin/env bash

# Exit immediately if any command below fails.
set -e

echo "Generating a slides directory.."

mkdir -p slides
rm -f slides/*

cd material
for f in *; do
  cd $f
  for s in *.pdf; do
    if [[ $s != "*.pdf" ]]; then
      if [[ $s == "slides.pdf" ]]; then
        ln $s ../../slides/${f}.pdf
      else
        ln $s ../../slides/${f}-${s}
      fi
    fi
  done
  cd ..
done
cd ..
