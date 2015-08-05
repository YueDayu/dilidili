/**
 * Created by Yue Dayu on 2015/8/5.
 */

;(function() {
    var send_btn = $('#send-comment');
    var input = $('#input-comment');
    var video_id = $('#video-id').html();

    function show_error(msg) {
        var error = document.createElement('div');
        error.setAttribute('class', 'alert alert-danger alert-dismissible');
        error.setAttribute('role', 'alert');
        error.innerHTML = "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span \
                    aria-hidden='true'>&times;</span></button> \
                    <strong>Error!</strong>" + msg + "</div>";
        document.getElementById('show-comment-error').innerHTML = "";
        document.getElementById('show-comment-error').appendChild(error);
    }

    function check() {
        str = input.val();
        if (str == "") {
            show_error("请输入内容");
            input.focus();
            return false;
        } else if (str.length > 400) {
            show_error("输入内容太长");
            input.focus();
            return true;
        }
        return true;
    }

    send_btn.click(function() {
        if (check()) {
            $.post('/video-add-comment/', {
                'id': video_id,
                'content': input.val()
            }, function(data) {
                if (!data['res']) {
                    show_error(data['error'])
                }
            });
            input.val("")
        }
    });
})();