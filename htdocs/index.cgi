#!/bin/sh

echo Content-Type: text/html
echo
for a in `ls *.*`;do
	echo "<hr>"
	echo "<div><a href=\"./$a\" target=\"_blank\">$a (Relative)</a></div>"
	echo "<div><a href=\"/$a\" target=\"_blank\">$a (Absolute)</a></div>"
	echo "<div><a href=\"//$HTTP_HOST/$a\" target=\"_blank\">$a (Full, Inherit schema)</a></div>"
	echo "<div><a href=\"http://$HTTP_HOST/$a\" target=\"_blank\">$a (Full HTTP)</a></div>"
	echo "<div><a href=\"https://$HTTP_HOST/$a\" target=\"_blank\">$a (Full HTTPS)</a></div>"
done
