#!/bin/sh

sid='t02K_14r6u3caN5X0FgpBLYbbivJspRpWz_OiBs5tGpKnscEhjqqJb_SVDdoVLMhafIm-kqbuRTiMfVz15MxIfKHqVyPamO6JE8wmExcnvlV8k'

test_url='http://set3.mail.qq.com/cgi-bin/mail_list?sid='$sid'&pagesize=100&folderid=1&page=1&s=inbox&showinboxtop=1&loc=folderlist,,,1'
verify_url='https://ssl.captcha.qq.com/cap_union_new_verify'
curl -vvvv  --cookie ./login.cookies "$test_url"




