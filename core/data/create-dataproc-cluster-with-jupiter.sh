#!/usr/bin/env bash


# change yur project-name
# single node w/anaconda and jupyter
gcloud dataproc clusters create spark-standalone-1 \
                --region europe-west3 \
                --subnet default \
                --zone europe-west3-a \
                --single-node \
                --master-machine-type n1-standard-4 \
                --master-boot-disk-size 30 \
                --image-version 1.4-debian9 \
                --project sandbox-236618
