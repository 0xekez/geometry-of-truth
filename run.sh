#!/bin/bash

function teardown() {
    deactivate
}

function setup() {
    source topology/bin/activate
}

function freeze() {
    setup
    pip freeze > requirements.txt
}

function experiment() {
    local dataset=$1
    setup
    python3 experiment.py $dataset
    gnuplot -e "filename='$dataset.csv'" plot-projection.gnuplot > $dataset.svg
    gnuplot -e "filename='$dataset-residuals.csv'" plot-residuals.gnuplot > $dataset-residuals.svg
    open $dataset.svg
    open $dataset-residuals.svg
}

case $1 in
    freeze)
	freeze
	;;
    experiment)
	experiment $2
	;;
    *)
	echo "usage: $0 <freeze/chatbot/experiment> <experiment:dataset>"
	;;
esac
