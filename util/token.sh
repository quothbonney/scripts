#!/usr/bin/bash


while getopts s: flag
do
	case "${flag}" in
		s) export GIT_TOKEN=${OPTARG};;
	esac
done

export PATH=$PATH:$GIT_TOKEN

echo $GIT_TOKEN | xclip -selection clipboard;

echo $GIT_TOKEN;
