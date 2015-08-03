/**
 * Created by Yue Dayu on 2015/8/4.
 */
function show_error(msg) {
    var error = document.createElement('div');
    error.setAttribute('class', 'alert alert-danger alert-dismissible');
    error.setAttribute('role', 'alert');
    error.innerHTML = "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span \
                    aria-hidden='true'>&times;</span></button> \
                    <strong>Error!</strong>" + msg + "</div>";
    document.getElementById('show-error').innerHTML = "";
    document.getElementById('show-error').appendChild(error);
}

function validate_required(field, alerttxt) {
    with (field) {
        if (value == null || value == "") {
            show_error(alerttxt);
            return false
        }
        else {
            return true
        }
    }
}

function check_password(field) {
    with (field) {
        if (value == null || value == "") {
            show_error("请填写密码");
            return false;
        } else if (value.length < 6) {
            show_error("密码长度太短");
            return false;
        }
        return true;
    }
}
