/**
 * Created by Yue Dayu on 2015/8/5.
 */

;
(function () {
    var send_btn = $('#send-bullet');
    var input = $('#input-bullet');
    var player = videojs('video');
    var video_id = $('#video-id').html();

    function show_error(msg) {
        var error = document.createElement('div');
        error.setAttribute('class', 'alert alert-danger alert-dismissible');
        error.setAttribute('role', 'alert');
        error.innerHTML = "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span \
                    aria-hidden='true'>&times;</span></button> \
                    <strong>Error!</strong>" + msg + "</div>";
        document.getElementById('show-bullet-error').innerHTML = "";
        document.getElementById('show-bullet-error').appendChild(error);
    }

    function hexFromRGB(r, g, b) {
        var hex = [
            r.toString(16),
            g.toString(16),
            b.toString(16)
        ];
        $.each(hex, function (nr, val) {
            if (val.length === 1) {
                hex[nr] = "0" + val;
            }
        });
        return hex.join("").toUpperCase();
    }

    function refreshSwatch() {
        var red = $("#red").slider("value"),
            green = $("#green").slider("value"),
            blue = $("#blue").slider("value"),
            hex = hexFromRGB(red, green, blue);
        $("#swatch").css("background-color", "#" + hex);
    }

    $(function () {
        $("#red, #green, #blue").slider({
            orientation: "horizontal",
            range: "min",
            max: 255,
            value: 127,
            slide: refreshSwatch,
            change: refreshSwatch
        });
        $("#red").slider("value", 255);
        $("#green").slider("value", 140);
        $("#blue").slider("value", 60);
    });

    function check() {
        str = input.val();
        if (str == "") {
            show_error("请输入内容");
            input.focus();
            return false;
        } else if (str.length > 200) {
            show_error("输入内容太长");
            input.focus();
            return true;
        }
        return true;
    }

    send_btn.click(function () {
        if (check()) {
            var red = $("#red").slider("value"),
                green = $("#green").slider("value"),
                blue = $("#blue").slider("value"),
                hex = hexFromRGB(red, green, blue);
            $.post('/video-add-bullet/', {
                id: video_id,
                time: parseInt(player.currentTime() * 1000),
                content: input.val(),
                color: "#" + hex
            }, function(data) {
                if (data['res'] == false) {
                    show_error(data['error']);
                }
            });
            input.val("");
        }
    });
})();