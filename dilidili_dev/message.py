__author__ = 'Yue Dayu'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .users import User
from .models import Message
from django.http import Http404


def inbox(request):
    if request.user.is_authenticated():
        sendmsg = Message.objects.filter(user_from=request.user).order_by('-time')
        receivemsg = Message.objects.filter(user_to=request.user).order_by('-time')
        userlist = []
        for x in sendmsg:
            userlist.append(x.user_to)
        for x in receivemsg:
            userlist.append(x.user_from)
        userlist = {}.fromkeys(userlist).keys()
        res_list = []
        for x in userlist:
            temp = {
                'user': x,
                'num': receivemsg.filter(user_from=x, status=False).count()
            }
            res_list.append(temp)
        return render(request, 'message/message.html', {'list': res_list})
    else:
        return HttpResponseRedirect('/login/')


def sendto(request, user_id):
    if request.user.is_authenticated():
        try:
            to_user = User.objects.get(id=user_id)
            if to_user == request.user:
                return HttpResponseRedirect('/inbox/')
            if request.method == 'POST':
                if request.POST['content'] and request.POST['content'] != "":
                    m = Message(user_from=request.user,
                                user_to=to_user,
                                content=request.POST['content'])
                    m.save()
                    return HttpResponseRedirect('/sendto/' + str(user_id))
            sendmsg = Message.objects.filter(user_from=request.user, user_to=to_user).order_by('-time')
            receivemsg = Message.objects.filter(user_to=request.user, user_from=to_user).order_by('-time')
            for x in receivemsg:
                x.status = True
                x.save()
            msg = sendmsg | receivemsg
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'message/sendto.html', {'to_user': to_user,
                                                       'msg_set': msg})
    else:
        return HttpResponseRedirect('/login/')


def del_msg(request, user_id, msg_id):
    if request.user.is_authenticated():
        try:
            msg = Message.objects.get(pk=msg_id)
            if msg.user_from == request.user and msg.user_to.id == int(user_id):
                msg.delete()
            return HttpResponseRedirect('/sendto/' + str(user_id))
        except Message.DoesNotExist:
            raise Http404("Message does not exist")
    else:
        return HttpResponseRedirect('/login/')
