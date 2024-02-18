#!/bin/bash

app_dir="app"
docs_dir="docs/methods"

rm -rf "$docs_dir"
mkdir -p "$docs_dir"

# find all .py files in app_dir, ignore tests and models
find "$app_dir" -name "*.py" ! -path "*/tests/*" ! -name "__init__.py" | while read pyfile; do
    # get relative path to file from app_dir
    relpath=${pyfile#$app_dir/}
    
    # convert to .md and prepend with docs_dir
    mdfile="$docs_dir/${relpath%.py}.md"
    
    # get path to directory
    mddir=$(dirname "$mdfile")
    
    # create directory if it doesn't exist
    mkdir -p "$mddir"
    
    # replace / with . for python module path
    modulepath=${relpath//\//.}
    modulepath=${modulepath%.py}
    
    # write module path to file
    echo "::: $modulepath" > "$mdfile"
done

# find all directories under app_dir
find "$app_dir" -type d | while read dir; do
    # if directory contains .py files, add __init__.py
    if find "$dir" -maxdepth 1 -name "*.py" -print -quit | grep -q .; then
        touch "$dir/__init__.py"
    fi
done
