#!/bin/bash

eval "$HTTP_COOKIE"

echo Content-Type: text/plain
echo Set-Cookie: a=${a:-$RANDOM}
echo Set-Cookie: b=${b:-$RANDOM}\; domain=$HTTP_HOST
echo Set-Cookie: c=${c:-$RANDOM}\; domain=$HTTP_HOST\; path=/
echo Set-Cookie: d=${d:-$RANDOM}\; domain=`echo $HTTP_HOST|sed 's/^\w*\.//'`
echo Set-Cookie: e=${e:-$RANDOM}\; domain=`echo $HTTP_HOST|sed 's/^\w*//'`
echo Set-Cookie: f=${f:-$RANDOM}\; domain=`echo $HTTP_HOST|sed 's/^\w*/\*/'`
echo Set-Cookie: g=${g:-$RANDOM}\; domain=www.google.com
echo
echo HTTP_HOST=$HTTP_HOST
echo HTTP_COOKIE=$HTTP_COOKIE
echo
echo $HTTP_COOKIE|sed 's/;\s*/\n/g'
