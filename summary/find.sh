#!/bin/bash

# Search word in files of this directory

read -p "Enter search word: " search_word

search_directory=$(pwd)

search_in_directory() {
  local directory="$1"
  local word="$2"

  for file in "$directory"/*; do
    if [ -d "$file" ]; then
      search_in_directory "$file" "$word"
    elif [ -f "$file" ]; then
      if grep -q "$word" "$file"; then
        echo "Match found in file: $file"
        grep "$word" "$file"
      fi
    fi
  done
}

search_in_directory "$search_directory" "$search_word"
