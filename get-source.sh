#!/bin/sh
# Usage:
# ./get-source.sh
# Author: Elan Ruusamäe <glen@pld-linux.org>
#
# Idea based on omnibus-software jre package
# https://github.com/opscode/omnibus-software/blob/master/config/software/jre.rb

package=instantclient
specfile=oracle-$package.spec
arch=$1

# abort on errors
set -e
# work in package dir
dir=$(dirname "$0")
cd "$dir"

arch=${1:-$(rpm -E %_arch)}

case "$arch" in
i686)
	refurl=http://www.oracle.com/technetwork/topics/linuxsoft-082809.html
	cookie=accept-ic_linux32-cookie
	;;
x86_64)
	refurl=http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
	cookie=accept-ic_linuxx8664-cookie
	;;
*)
	echo >&2 "arch not recognized"
	exit 1
	;;
esac

cat <<EOF

You must accept the OTN Development and Distribution License Agreement for
Instant Client to download this software.

http://www.oracle.com/technetwork/licenses/instant-client-lic-152016.html

Press "ENTER" to Accept License Agreement
Press Ctrl-C to Decline License Agreement

EOF
read license

urls=$(builder -su *.spec --target $arch | grep http://)
for url in $urls; do
	wget -c --header "Cookie: oraclelicense=$cookie; gpw_e24=$refurl" "$url"
done
