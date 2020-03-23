#!/bin/sh

set -eu

autoclean() {
    echo "cleaning files older than 1 day..."
    find /tmp -type f -mtime +1 -print -delete
}

# background tasks
(
    set -eu
    while true; do
        # exec in subshell so we don't die
        ( autoclean ) || :
        sleep 120
    done
) &

exec "$@"
