from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        # profile의 객체를 받는데 여기서 pk는 profileapp => urls.py에서 update로 받는 pk를 받아서 해당 profile의 주인을 확인 한다.
        if not profile.user == request.user:  # 만약 profile의 user가 request(요청)을 보내는 user와 맞지 않으면 (주인이 아니면)
            return HttpResponseForbidden() # 접근에 제한을 준다.
        return func(request, *args, *kwargs) # 그렇지 않고 요청한 user와 해당 웹의 user(주인)가 맞다면 정상적으로 보여준다.
    return decorated



