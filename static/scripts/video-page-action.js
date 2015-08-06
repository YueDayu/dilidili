/**
 * Created by Yue Dayu on 2015/8/6.
 */

;(function(){
    var video_id = $('#video-id').html();
    var collect_btn = $('#collect-btn');
    var like_btn = $('#like-btn');
    var money_btn = $('#money-btn');

    collect_btn.click(function() {
        $.post('/video-set-collcetion/', {
            id: video_id
        }, function(data) {
            if (data['res']) {
                var show = $('#collect-text');
                if (data['flag']) {
                    show.html("已收藏");
                } else {
                    show.html('收藏');
                }
            }
        });
    });

    like_btn.click(function() {
        $.post('/video-set-like/', {
            id: video_id
        }, function(data) {
            if (data['res']) {
                var show = $('#like-text');
                if (data['flag']) {
                    show.html("取消赞");
                    show.removeClass('like-no');
                    show.addClass('like-yes');
                } else {
                    show.html('赞');
                    show.removeClass('like-yes');
                    show.addClass('like-no');
                }
            }
        });
    });

    money_btn.click(function() {
        var r = confirm("确定投喂一枚硬币么？");
        if (r) {
            $.post('/video-add-money/', {
                id: video_id
            }, function(data) {
                var show = $('#money-num');
                if (data['res']) {
                    show.html(data['video_money']);
                } else {
                    alert(data['error']);
                }
            });
        }
    });
})();