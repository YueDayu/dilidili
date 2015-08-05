;(function() {
	var search_field = "name";
	var search_category = "";
	var search_orderby = "-time";

	var input_text = $("#input-text");
	var btn_search = $("#btn-search");

	var selected_field_elem = $("#tab-name");
	var selected_cat_elem = $("#cat-all");

	btn_search.click(function(event) {
		btn_search.attr("disabled", true);
		var form_data = { "order_by": search_orderby, "status": 0 };
		form_data[search_field + "__icontains"] = input_text.val();

		if (search_category != "") {
			form_data["category_set__id"] = search_category;
		}

		$.get("/search/resulthtml/", form_data, function(data) {
			$("#result-container").html(data);
		}).always(function(){
			btn_search.attr("disabled", false);
		});
	});

	$("#tab-name").click(function (event) {
		selected_field_elem.removeClass("active");
		selected_field_elem = $("#tab-name").addClass("active");
		search_field = "name";
		btn_search.trigger("click");
	});

	$("#tab-owner").click(function (event) {
		selected_field_elem.removeClass("active");
		selected_field_elem = $("#tab-owner").addClass("active");
		search_field = "owner__name";
		btn_search.trigger("click");
	});

	$("#tab-tag").click(function (event) {
		selected_field_elem.removeClass("active");
		selected_field_elem = $("#tab-tag").addClass("active");
		search_field = "tag";
		btn_search.trigger("click");
	});

	window.click_cat = function(cat_id) {
		selected_cat_elem.removeClass("active");
		selected_cat_elem = $("#cat-" + cat_id).addClass("active");
		search_category = cat_id;
		btn_search.trigger("click");
	};

	$("#cat-all").click(function(event) {
		selected_cat_elem.removeClass("active");
		selected_cat_elem = $("#cat-all").addClass("active");
		search_category = "";
		btn_search.trigger("click");
	});

	window.click_sort = function(sort_by) {
		$("#dropdown-sort").html($("#sortby" + sort_by).text() + "<span class='caret'></span>");
		search_orderby = sort_by;
		btn_search.trigger("click");
	};

	btn_search.trigger("click");

})();
