;(function () {
	var perm_upload = $("#btn-perm-upload");
	var perm_comment = $("#btn-perm-comment");
	var perm_bullet = $("#btn-perm-bullet");

	perm_upload.click(function (e) {
		perm_upload.attr("disabled", true);
		$.post("admin/toggleupload/", function(data) {
			if (perm_upload.hasClass("btn-danger")) {
				perm_upload.removeClass("btn-danger")
						   .addClass("btn-success")
						   .html("解除视频封禁");
			} else {
				perm_upload.removeClass("btn-success")
						   .addClass("btn-danger")
						   .html("封禁视频");
			}
		}).always(function() {
			perm_upload.attr("disabled", false);
		});
	});

	perm_comment.click(function (e) {
		perm_comment.attr("disabled", true);
		$.post("admin/togglecomment/", function(data) {
			if (perm_comment.hasClass("btn-danger")) {
				perm_comment.removeClass("btn-danger")
						   .addClass("btn-success")
						   .html("解除评论封禁");
			} else {
				perm_comment.removeClass("btn-success")
						   .addClass("btn-danger")
						   .html("封禁评论");
			}
		}).always(function() {
			perm_comment.attr("disabled", false);
		});
	});

	perm_bullet.click(function (e) {
		perm_bullet.attr("disabled", true);
		$.post("admin/togglebullet/", function(data) {
			if (perm_bullet.hasClass("btn-danger")) {
				perm_bullet.removeClass("btn-danger")
						   .addClass("btn-success")
						   .html("解除弹幕封禁");
			} else {
				perm_bullet.removeClass("btn-success")
						   .addClass("btn-danger")
						   .html("封禁弹幕");
			}
		}).always(function() {
			perm_bullet.attr("disabled", false);
		});
	});
})();
