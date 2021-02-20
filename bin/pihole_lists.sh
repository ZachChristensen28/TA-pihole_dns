#!/bin/bash
#
# Get Pi-hole lists to Splunk
#
PIHOLE_HOME='/etc/pihole'

test ! -d $PIHOLE_HOME && 1>&2 echo "msg=\"Unable to find $PIHOLE_HOME\"" && exit 1

for list in $(ls $PIHOLE_HOME | egrep "^list\."); do
        awk -v l=$list '{ print $1, l}' $PIHOLE_HOME/$list
done

exit $?
