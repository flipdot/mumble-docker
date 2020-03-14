#!/bin/bash
set -euxo pipefail

if [[ "$RENEWED_DOMAINS" == *"mumble.flipdot.org"* ]]; then
    cp -v $RENEWED_LINEAGE/{fullchain.pem,privkey.pem} /var/mumble/data/
docker restart mumble_mumble_1
else
    echo "ignoring $RENEWED_DOMAINS"
fi

