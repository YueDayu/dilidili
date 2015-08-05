;(function() {
	var btn_toggle = $("#btn-togglepublish");

	btn_toggle.click(function(event) {
		btn_toggle.attr("disabled", true);
		$.post("togglepublish/", function(data) {
			if (btn_toggle.hasClass("btn-danger")) {
				btn_toggle.removeClass("btn-danger").addClass("btn-success").text("审核通过");
			} else {
				btn_toggle.removeClass("btn-success").addClass("btn-danger").text("审核不通过");
			}
		}).always(function() {
			btn_toggle.attr("disabled", false);
		});
	});
})();
