#!/bin/bash
echo $1
for filename in $1/*.mp4; do
    ./process_video.sh $filename
done
