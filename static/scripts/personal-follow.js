;(function () {
	var btn_toggle = $("#toggle-follow");

	btn_toggle.click(function (e) {
		btn_toggle.attr("disabled", true);
		$.post("togglefollow/", function(data) {
			if (btn_toggle.hasClass("btn-default")) {
				btn_toggle.removeClass("btn-default")
						   .addClass("btn-primary")
						   .html("关注");
			} else {
				btn_toggle.removeClass("btn-primary")
						   .addClass("btn-default")
						   .html("取消关注");
			}
		}).always(function() {
			btn_toggle.attr("disabled", false);
		});
	});
})();
