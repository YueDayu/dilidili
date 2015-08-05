/**
 * Created by Yue Dayu on 2015/8/4.
 */

;
(function () {
    var player = videojs('video');

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
            console.log(data);
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
        setInterval(get_bullet, 1500);
    });
})();