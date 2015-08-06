;(function () {
	window.click_collection = function(event) {
		$.get("collection/", function(data) {
			var infopanel = $("<div class='dd-user-info'>");
			var infotitle = $("<div class='dd-user-title'>").html("<p>我的收藏</p>");
			var infocontent = $("<div id='main-content' class='box-inner clearfix'>").html(data);
			infopanel.append(infotitle).append(infocontent);
			$("#right-content").empty().append(infopanel);
		});
	};

	window.click_follow = function(event) {
		var followerpanel = $("<div class='dd-user-info'>");
		var followertitle = $("<div class='dd-user-title'>").html("<p>关注我的人</p>");
		var followercontent = $("<div id='main-content' class='box-inner clearfix'>");
		followerpanel.append(followertitle).append(followercontent);

		var followingpanel = $("<div class='dd-user-info'>");
		var followingtitle = $("<div class='dd-user-title'>").html("<p>我关注的人</p>");
		var followingcontent = $("<div id='main-content' class='box-inner clearfix'>");
		followingpanel.append(followingtitle).append(followingcontent);

		$("#right-content").empty().append(followingpanel).append(followerpanel);

		$.get("following/", function(data) {
			followingcontent.html(data);
		});

		$.get("follower/", function(data) {
			followercontent.html(data);
		});
	};

	window.click_home = function(event) {
		$.get("center/", function(data) {
			$("#right-content").html(data);
		})
	};

	window.click_upload_err = function(event) {
	    var error = document.createElement('div');
	    error.setAttribute('class', 'alert alert-danger alert-dismissible');
	    error.setAttribute('role', 'alert');
	    error.innerHTML = "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span \
	                    aria-hidden='true'>&times;</span></button> \
	                    <strong>Error!</strong>" + " 您已被封禁，不能上传视频" + "</div>";
	    document.getElementById('show-error').innerHTML = "";
	    document.getElementById('show-error').appendChild(error);
	    return false;
	};

	$("#nav-home").trigger("click");
})();
