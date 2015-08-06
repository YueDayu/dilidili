/**
 * Created by Yue Dayu on 2015/8/6.
 */

;(function(){
    var menu = $('#dropdownMenu1');
    var show = $('#msg-num');

    function get_read() {
        $.post('/unread-msg/', function(data) {
            console.log(data);
            if (data['num'] == 0) {
                menu.html("我的<span class='caret'></span>");
                show.html("私信");
            } else {
                menu.html("我的<span class='caret'></span><span class='num'>*</span>");
                show.html("私信<span class='num'>" + data['num'] + "</span>");
            }
        });
    }

    $(function() {
            get_read();
            setInterval(get_read, 10000);
        }
    )
})();