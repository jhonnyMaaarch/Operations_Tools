#!/bin/bash
# copying provided file to provided destination folder


if [ -f "$1" ] && [ -d "$2" ]; then
	cp -p $1 $2
        echo "File "$1" has been successfully copied into the folder "$2" "
        ls -al $2
else
	echo "Usage: ./file_copy.sh <file_to_copy> <destination_dir> "
	echo "check that you have this correctly placed, then retry. "
fi

