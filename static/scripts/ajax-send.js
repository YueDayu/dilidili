/**
 * Created by Yue Dayu on 2015/8/4.
 */

;(function () {
    $(document).ready(function () {
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                function getCookie(n) {
                    var cookieValue = null;
                    if (document.cookie && document.cookie != '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                            var cookie = jQuery.trim(cookies[i]);
                            if (cookie.substring(0, n.length + 1) == (n + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(n.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });
    });
})();
