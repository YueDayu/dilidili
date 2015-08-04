function reply(obj){
	$('.user-name')[0].innerHTML = $(obj).parents()[3].getAttribute("data-name");
}

function history(obj){
	$('#pm-history')[0].innerHTML = "";
	$('.user-name')[1].innerHTML = $(obj).parents()[3].getAttribute("data-name");
	/*对于每一条符合条件的私信，执行以下操作，将其按照时间倒序添加到私信页面上 for msg in msgs*/
	var his = $('#pm-history');
	var pmitem = $("<div class=\"dd-pm-item\"></div>").appendTo(his);
	var row = $("<div class=\"row\"></div>").appendTo(pmitem);
	//username 用户名 若为用户本人则为“我” user-link 用户主页链接 face-src 用户头像地址 msg 私信内容 msgdate 发送日期
	var username="Another";
	var userlink = "#";
	var facesrc = "hehe.jpg";
	var msg = "去去去没没没";
	var msgdate = "1月1日 12:00";
	var face = $("<div class=\"col-md-2 col-sm-2 col-xs-3\"><a href=" + userlink + "><img src=" + facesrc + " class=\"img-rounded\"/></a></div>").appendTo(row);
	var maincontent = $("<div class=\"col-md-10 col-sm-10 col-xs-9\"><a title=\"Another\" href=" + userlink + ">" + username + "</a>：</div>").appendTo(row);
	var msgcontent = $("<p>" + msg + "</p>").appendTo(maincontent);
	var date = $("<div class=\"dd-pm-item-meta\"><span class=\"dd-grey dd-left\">"+msgdate+"</span></div>").appendTo(maincontent);
}