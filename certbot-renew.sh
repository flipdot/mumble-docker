#!/bin/sh

certbot renew --force-renewal --deploy-hook /var/mumble/certbot-hook.sh

