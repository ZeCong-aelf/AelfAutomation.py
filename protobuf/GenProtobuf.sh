#!/bin/bash

protoc --python_out=./generate aelf/*.proto
protoc --python_out=./generate *.proto