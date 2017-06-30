#!/bin/sh

sid=$(cat sid |awk -F "\="  '{print $2}')
echo "sid is $sid"      
test_url='http://set3.mail.qq.com/cgi-bin/mail_list?sid='$sid'&pagesize=100&folderid=1&page=1&s=inbox&showinboxtop=1&loc=folderlist,,,1'
verify_url='https://ssl.captcha.qq.com/cap_union_new_verify'
echo curl -vvvv  --cookie ./verify_code.cookies \
     --cookie-jar login.cookies \
     --data-binary "'$(cat post_data)'" \
     $(cat ./http_header) \
     "$verify_url"


