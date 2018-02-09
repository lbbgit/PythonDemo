// ==UserScript==
// @name         add jquery
// @version      0.1
// @description  press [alt + j] add jquery
// @author       lbbgit
// @match        *://*/*
// @namespace    https://greasyfork.org/users/85375-lbbgit
// ==/UserScript==
(function() {  
    document.onkeydown = function(e) {
        // 设置监听按键
        // alert(e.keyCode)
        if (e.keyCode == 74 && e.altKey) { // 74:J 81:Q
            if(jQuery){
				alert('contains jquery now!');
				return;
			}
            //jquery min
			var d=document;
			var jq=d.createElement('script');  
			jq.s=jq.setAttribute;
			jq.s("type","text/javascript"); 
			jq.s("src", 'http://ajax.microsoft.com/ajax/jquery/jquery-1.4.min.js');
			d.getElementsByTagName("head")[0].appendChild(jq);
            
            return ; 
            //添加监听
            var colse = document.querySelector('#showQRcodeJs');
            colse.addEventListener('click',function() {
                document.body.removeChild(document.querySelector('#showQRcodeJs'));
            }, false);
        }
    };
    //insert other code here 
})();