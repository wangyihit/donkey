#!/usr/bin/env python
# encoding=utf-8

js_lib = """
(function(){
var bot = {};
function qqMailInputUserData(uname, upass){
    var uname_ele = document.querySelector("#u");
    uname_ele.value = uname;
    var upass_ele = document.querySelector("#p");
    upass_ele.value = upass;
}

function loginQQMail(uname, upass){
    // input user info
    qqMailInputUserData(uname, upass);
    // push login button
    var login_button = document.querySelector("#login_button");
    var e = document.createEvent('MouseEvent');
    e.initEvent('click', false, false);
    login_button.dispatchEvent(e);
}


bot.qqMailInputUserData = qqMailInputUserData;
bot.loginQQMail = loginQQMail;
window.bot = bot;


})();
"""