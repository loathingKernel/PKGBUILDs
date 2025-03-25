#!/usr/bin/python3

import os
import sys
import shutil
import subprocess
from pathlib import Path

workflows_folder = ".github/workflows/"
workflows_path = Path(workflows_folder)

workflow_base = """
name: {pkgname}

on:
  workflow_dispatch:
    inputs:
      action:
        description: "Repository action"
        required: true
        type: choice
        default: 'build'
        options:
          - 'build'
          - 'remove'
          - 'skip'
  push:
    branches:
      - master
    paths:
      - {subdir}/{pkgname}/.SRCINFO

jobs:
  repository:
    strategy:
      matrix:
        repository: [public]
    uses: ./.github/workflows/_job_pkgrepo.yml
    with:
      pkgdir: {subdir}/{pkgname}
      repository: ${{{{ matrix.repository }}}}
      action: ${{{{ inputs.action != '' && inputs.action || 'build' }}}}
"""

path = Path(sys.argv[1])
subdir = path.parent
pkgname = path.stem

workflow_file = workflows_path.joinpath(f"{pkgname}.yml")

with workflow_file.open("w") as wf:
    wf.write(workflow_base.format(
        subdir=subdir, pkgname=pkgname, repotag="public")
    )

subprocess.run(['git', 'add', workflow_file.as_posix()])
subprocess.run(['git', 'commit', '-m', f'workflows: add {pkgname}'])

