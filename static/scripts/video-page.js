/**
 * Created by Yue Dayu on 2015/8/4.
 */

;(function() {
    var player = videojs('video');

    var send_play = function() {
        $.post('/video-add-play/', {'id': window.location.pathname.split('/')[2]}, function(data) {
            console.log(data);
            // TODO: error process
        });
    };

    player.one('play', send_play);
})();