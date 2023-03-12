#!/bin/bash

# This script create and delete a directory

echo -n "Give the name of the folder : "
read folderName

if [ -e $folderName ]; then
 echo This folder already exists !
 exit 0
fi

currentDir=$(pwd)

echo "Folder creation ..."
sleep 2
mkdir $currentDir/$folderName

echo $currentDir/$folderName created

echo $currentDir/$folderName deletion...
sleep 2
rm -rf $currentDir/$folderName
