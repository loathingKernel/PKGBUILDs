#!/bin/bash
set -euo pipefail

echo "pkgdir:         ${INPUT_PKGDIR:-.}"
echo "release_repo:   ${INPUT_REPORELEASETAG:-}"

FILE="$(basename "$0")"

# Makepkg does not allow running as root
# Create a new user `builder`
# `builder` needs to have a home directory because some PKGBUILDs will try to
# write to it (e.g. for cache)
useradd builder -m
# When installing dependencies, makepkg will use sudo
# Give user `builder` passwordless sudo access
echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Give all users (particularly builder) full access to these files
chmod -R a+rw .

BASEDIR="$PWD"
cd "${INPUT_PKGDIR:-.}"

function download_database () {
	# Download the repository files if a repository tag has been specified
	# This is put here to fail early in case they weren't downloaded
	REPOFILES=("${INPUT_REPORELEASETAG:-}".{db{,.tar.gz},files{,.tar.gz}})
	for REPOFILE in "${REPOFILES[@]}"; do
		sudo -u builder curl \
			--retry 5 --retry-delay 30 --retry-all-errors \
			--location --fail \
			-o "$REPOFILE" "$GITHUB_SERVER_URL"/"$GITHUB_REPOSITORY"/releases/download/"${INPUT_REPORELEASETAG:-}"/"$REPOFILE"
	done
	# Delete the `<repo_name>.db` and `repo_name.files` symlinks
	rm "${INPUT_REPORELEASETAG:-}".{db,files} || true
}

if [ -n "${INPUT_REPORELEASETAG:-}" ]; then
	# Download database files to test for availability
	download_database
	# Delete them because they will be downloaded again
	rm "${INPUT_REPORELEASETAG:-}".{db,files}.tar.gz
fi

# Assume that if .SRCINFO is missing then it is generated elsewhere.
# AUR checks that .SRCINFO exists so a missing file can't go unnoticed.
if [ -f .SRCINFO ] && ! sudo -u builder makepkg --printsrcinfo | diff - .SRCINFO; then
	echo "::error file=$FILE,line=$LINENO::Mismatched .SRCINFO. Update with: makepkg --printsrcinfo > .SRCINFO"
	exit 1
fi

# Make the builder user the owner of these files
# Without this, (e.g. only having every user have read/write access to the files),
# makepkg will try to change the permissions of the files itself which will fail since it does not own the files/have permission
# we can't do this earlier as it will change files that are for github actions, which results in warnings in github actions logs.
chown -R builder .

# Get array of packages to be built
# shellcheck disable=SC2086
# shellcheck disable=SC2154
# shellcheck disable=SC2001
mapfile -t PKGNAMES < <(source PKGBUILD && echo "${pkgname[@]}" | sed 's/ /\n/g' )
echo "Package name(s): ${PKGNAMES[*]}"

if [ -n "${INPUT_REPORELEASETAG:-}" ]; then
	# Download database files again in case another action updated them in the meantime
	download_database
	# Create package file list for the old database
	zcat "${INPUT_REPORELEASETAG:-}".db.tar.gz | strings | grep '.pkg.tar.' | sort > old_db.packages
fi

i=0
for PKGNAME in "${PKGNAMES[@]}"; do
	if [ -n "${INPUT_REPORELEASETAG:-}" ]; then
		sudo -u builder repo-remove "${INPUT_REPORELEASETAG:-}".db.tar.gz "$PKGNAME"
	else
		echo "Skipping repository update for $RELPKGFILE"
	fi
	(( ++i ))
done

if [ -n "${INPUT_REPORELEASETAG:-}" ]; then
	# Delete the `<repo_name>.db` and `repo_name.files` symlinks
	rm "${INPUT_REPORELEASETAG:-}".{db,files}
	# Copy repo archives to their suffix-less symlinks because symlinks are not uploaded to GitHub releases
	cp "${INPUT_REPORELEASETAG:-}".db{.tar.gz,}
	cp "${INPUT_REPORELEASETAG:-}".files{.tar.gz,}
	REPOFILES=("${INPUT_REPORELEASETAG:-}".{db{,.tar.gz},files{,.tar.gz}})
	j=0
	for REPOFILE in "${REPOFILES[@]}"; do
		RELREPOFILE="$(realpath --relative-base="$BASEDIR" "$(realpath -s "$REPOFILE")")"
		echo "repofile$j=$RELREPOFILE" >> $GITHUB_OUTPUT
		(( ++j ))
	done
	# List package files removed from the database
	zcat "${INPUT_REPORELEASETAG:-}".db.tar.gz | strings | grep '.pkg.tar.' | sort > new_db.packages
	k=0
	for OLDFILE in $(diff {old,new}_db.packages | grep -E "^<" | cut -c3-);do
		echo "oldfile$k=$OLDFILE" >> $GITHUB_OUTPUT
		(( ++k ))
	done
fi
