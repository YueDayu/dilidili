/**
 * Created by Yue Dayu on 2015/8/4.
 */

;
(function () {
    var player = videojs('video');
    var show_comment_btn = $('#show-comment-btn');
    var video_id = $('#video-id').html();

    var max = 0;

    var send_play = function () {
        $.post('/video-add-play/', {'id': video_id}, function (data) {
            console.log(data);
        });
    };

    function add_bullet(item) {
        c = document.createElement('tr');
        c.innerHTML = "<td class='col1'>" + item.content + "</td><td><time>" + item.send_date + "</time></td>"
        $('#bullet-collect').append(c);
    }

    function get_bullet() {
        $.post('/video-get-bullet/', {
            id: video_id,
            last: max
        }, function (data) {
            if (data['res']) {
                max = data['max'];
                for (var x in data['list']) {
                    add_bullet(data['list'][x]);
                    window.show_bullet_ready.push(data['list'][x]);
                }
            }
        });
    }

    player.one('play', send_play);
    $(document).ready(function () {
        setInterval(get_bullet, 2000);
    });

    function add_comment(item) {
        var del_btn = item['can_del'] ? "<a class='cm-del-btn' onclick='del_cmt(" + item['comment_id']
            + ")'>删除</a>" : "";
        var c = document.createElement('div');
        c.setAttribute('id', 'comment-' + item['comment_id']);
        c.setAttribute('class', 'comment panel panel-default');
        c.innerHTML = "<div class='row'> <div class='col-md-1 col-sm-1 col-xs-2'>" +
            "<a href='/personal/" + item['user_id'] +
            "' target='blank'> <div class='facebox'> " +
            "<img src='" + item['user_image'] + "' " +
            "class='img-rounded'/> </div> </a> </div>" +
            "<div class='col-md-11 col-sm-11 col-xs-10'> <div class='comm-author'>" +
            "<a href='/personal/" + item['user_id'] + "' target='blank'>" +
            item['user_name'] + "</a></div><div class='content'>" + item['comment_context'] +
            "</div> <div class='comm-info'>" + item['comment_time'] + del_btn + "</div> </div> </div>";
        $('#comment-area').append(c);
    }

    function add_no_comment(str) {
        var c = document.createElement('div');
        c.setAttribute('class', 'comment panel panel-default no-comment');
        c.innerHTML = str + "<a onclick='comment_refresh()' class='cm-del-btn' id='comment-refresh'>点我刷新</a>";
        $('#comment-area').append(c);
    }

    window.comment_refresh = function () {
        $.post('/video-get-comment/', {
            id: video_id
        }, function(data) {
            if (data['res']) {
                show_comment_btn.hide();
                if (data['list'].length == 0) {
                    $('#comment-area').empty();
                    add_no_comment("暂时没有评论");
                } else {
                    $('#comment-area').empty();
                    for (var x in data['list']) {
                        add_comment(data['list'][x]);
                    }
                    add_no_comment("一共" + data['list'].length + "条评论。");
                }
            }
        });
    };

    show_comment_btn.click(function() {
        comment_refresh();
    });

    window.del_cmt = function(id) {
        var r = confirm("您要删除这条评论么？");
        if (r) {
            $.post('/video-del-comment/', {
                id: id
            }, function (data) {
                if (data['res']) {
                    $('#comment-' + id).remove();
                }
            });
        }
    }
})();