# Lawless

Published notes for fantasy western D&D campaign set in Columbia (World Anew).

See <https://ztomasze.github.io/dnd-lawless/> for the published version.


## Editing

The repo is currently configured (in `config/local_config.sh`) to point to my master Obsidian version, which contains both public and private material.  Running `bin/local_build.sh` will then pull those changes into this repo (into `src`) and build them using Quartz to create `docs/`.

If you want to make changes directly to the public content published here, you can:

+ Clone this repo
+ Pull in the necessary Quartz files: `git submodule init`
+ Edit `config/local_config.sh` to point directly to `src`
+ Make your edits in `src/`
+ Rebuild: `bin/local_build.sh`
+ Check what you built: `bin/local_serve.sh`
+ Submit a PR of your changes on a fresh branch

On my end, I can then:

+ Update `main` in GitHub to reflect the latest view of my local (master) Obsidian state
+ Merge your branch and resolve any conflicts
+ Rsync the changed files back into the Obsidian vault
