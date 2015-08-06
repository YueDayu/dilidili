/**
 * Created by Yue Dayu on 2015/8/4.
 */

// example:
//    show_bullet_ready.push(
//        {
//            time: player.currentTime() * 1000 + 200,
//            send_data: 111,
//            content: "测试",
//            color: "#ffffff"
//        }
//    );

;
(function () {
    'use strict';

    var player = null;
    var height = 0;
    var width = 0;
    var c = null;
    var video = null;
    var cxt = null;
    var num = 0;

    var show_loop;

    var ready = [];
    var no_ready = [];
    var show = [];
    var lines = [];

    var slider = null;
    var slider_btn = null;

    var init = function () {
        slider = $('#slider');
        slider.slider({
            orientation: "horizontal",
            range: "min",
            max: 99,
            value: 100,
            change: refresh
        });
        slider_btn = $('#is_show');
        player = videojs('video');
        c = document.createElement('canvas');
        video = $('#video');
        c.setAttribute('id', 'canvas_show');
        height = video.height();
        width = video.width();
        c.setAttribute('height', height.toString());
        c.setAttribute('width', width.toString());
        video.append(c);
        cxt = c.getContext("2d");
        cxt.fillStyle = "#FF0000";
        cxt.font = "26px 黑体";
        set_lines();

        player.on('fullscreenchange', function () {
            on_window_change();
        });

        $(window).on('resize', function () {
            on_window_change();
        });

        player.on('play', function () {
            start();
        });

        player.on('pause', function () {
            stop();
        });

        player.on('ended', function () {
            ready = ready.concat(no_ready);
            no_ready.length = 0;
            stop();
            set_lines();
            show.length = 0;
        });

        player.on('seeked', function () {
            seeked(player.currentTime());
            clear();
            set_lines();
            show.length = 0;
        });

        slider_btn.click(function () {
            btn_click();
        });
    };

    function btn_click() {
        if (slider_btn.hasClass("active")) {
            slider_btn.toggleClass("active", false);
            slider.slider({
                value: 0
            });
        } else {
            slider_btn.toggleClass("active", true);
            slider.slider({
                value: 99
            });
        }
        refresh();
    }

    function refresh() {
        var val = slider.slider("value");
        if (val == 0) {
            slider_btn.toggleClass("active", false);
        } else {
            slider_btn.toggleClass("active", true);
        }
        c.setAttribute("style", "opacity:" + (val / 100));
    }

    function on_window_change() {
        clear();
        height = video.height();
        width = video.width();
        c.setAttribute('height', height.toString());
        c.setAttribute('width', width.toString());
        cxt.font = "26px 黑体";
        set_lines();
    }

    function start() {
        show_loop = setInterval(draw_lines, 10);
    }

    function stop() {
        clearInterval(show_loop);
    }

    function set_lines() {
        num = parseInt(height / 28);
        lines.length = num;
        for (var i = 0; i < num; i++) {
            lines[i] = 0;
        }
    }

    function clear() {
        cxt.clearRect(0, 0, width, height);
    }

    function add_to_show() {
        ready.sort(function (a, b) {
            return a.time - b.time;
        });
        for (var i = 0; i < ready.length; i++) {
            var temp;
            if (ready[0].time < player.currentTime() * 1000) {
                temp = ready.shift();
                no_ready.push(temp);
                temp['width'] = cxt.measureText(temp.content).width + 3;
                temp['x'] = width;
                var min = lines[0];
                var index = 0;
                for (var j = 1; j < num; j++) {
                    if (lines[j] < min) {
                        min = lines[j];
                        index = j;
                    }
                }
                lines[index]++;
                temp['y'] = 28 * (index + 1) + 1;
                temp['index'] = index;
                temp['is_pass'] = false;
                temp['speed'] = Math.log(temp.width) / 2;
                show.push(temp);
            } else {
                break;
            }
        }
    }

    var flag = true;

    function delete_from_show() {
        show.sort(function (a, b) {
            return (a.x + a.width) - (b.x + b.width);
        });
        if (flag && show.length == 4) {
            flag = false;
        }
        for (var i = 0; i < show.length; i++) {
            if (show[0].x + show[0].width < 0) {
                show.shift();
            } else {
                break;
            }
        }
        for (var j = show.length - 1; j >= 0; j--) {
            if (show[j].x + show[j].width < width && show[j].is_pass == false) {
                lines[show[j].index]--;
                show[j].is_pass = true;
            }
        }
    }

    function draw_lines() {
        add_to_show();
        clear();
        for (var i = 0; i < show.length; i++) {
            show[i].x -= show[i].speed;
            cxt.fillStyle = show[i].color;
            cxt.fillText(show[i].content, show[i].x, show[i].y);
        }
        delete_from_show();
    }

    function seeked(time) {
        no_ready.sort(function (a, b) {
            return b.time - a.time;
        });
        var temp;
        while (no_ready.length > 0) {
            if (no_ready[0].time > time * 1000) {
                temp = no_ready.shift();
                ready.push(temp);
            } else {
                break;
            }
        }
        ready.sort(function (a, b) {
            return a.time - b.time;
        });
        while (ready.length > 0) {
            if (ready[0].time < time * 1000) {
                temp = ready.shift();
                no_ready.push(temp);
            } else {
                break;
            }
        }
    }

    init();

    window.show_bullet_ready = ready;
})();