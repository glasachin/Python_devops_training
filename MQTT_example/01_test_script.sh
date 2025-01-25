#! /bin/bash
for i in {1..100}; do
    echo "Running iteration $i"
    mosquitto_pub -h "14.195.107.2" -p 8002 -t "kimbal/nilm/dev" -m "$i : Hello Sachin"
done