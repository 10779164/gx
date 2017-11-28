function auth(){
        hostname=document.getElementById("hostname").value;
        ip=document.getElementById("ip").value;
        passwd_root=document.getElementById("passwd_root").value;
        passwd_db=document.getElementById("passwd_db").value;
        ssh_port=document.getElementById("ssh_port").value;
        other=document.getElementById("other").value;
        if (hostname==""){
                alert("主机名不能为空");
                document.getElementById("hostname").focus();
		return false;
        }
   	var reg=/^(\d{1,3}|\*)\.(\d{1,3}|\*)\.(\d{1,3}|\*)\.(\d{1,3}|\*)$/g;
	if ( reg.test(ip) ) {
	}
	else{
		alert("请输入正确的IP地址！");
		return false;
	}
	
	if( ssh_port>=0 && ssh_port<=65535 && port!=""){
	}
	else{
		alert("ssh端口范围为：0~65535");
		return false;
	}	
}

