#!/usr/bin/env python3

from subprocess import call
import sys
import os
from time import gmtime, strftime
import pprint as pp

def identify_files(cwd,repos):

    ignore = ['.vscode','.git','.DS_Store']

    repoList = []
    for repo in repos:
        d = {}
        d['repo'] = repo
        d['folders'] = {}
        
        files = os.listdir(os.path.join(cwd,repo))
        for f in files:
            if os.path.isdir(os.path.join(cwd,repo,f)): 
                if not f[0] == '.':
                    d['folders'][f] = []
                    subfiles = os.listdir(os.path.join(cwd,repo,f))
                    for sub in subfiles:
                        d['folders'][f].append(sub)

        repoList.append(d)

    return repoList

def get_repo_folders(cwd):
    repos = []

    # if there is a .git folder in this directory, then handle only it
    if os.path.isdir(os.path.join(cwd,'.git')):
        return [cwd]

    # otherwise get all the folders in this directory that are repos
    all = os.listdir(cwd)

    print(all)
    
    for f in all:
        if os.path.isdir(os.path.join(cwd,f,'.git')): 
            repos.append(f)

    return repos

def printUsage():
    print('Usage: ??')
    sys.exit(0)

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #      printUsage()

    # Get the directory of the folder your in.
    cwd = os.getcwd()
    cwd = "/Users/griffin/code/2020_courses"

    repos = get_repo_folders(cwd)
    
    files_dict = identify_files(cwd,repos)

    pp.pprint(files_dict)
