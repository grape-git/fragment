from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk']) # user 변수에 User 모델의 객체를 넣는데 요청을 받으면서 primarykey로 받은 값을 가지고 있는 user 객체
        if not user == request.user:  # 만약 요청한 user와 해당 웹의 user가 아니라면
            return HttpResponseForbidden() # 접근에 제한을 준다.
        return func(request, *args, *kwargs) # 그렇지 않고 요청한 user와 해당 웹의 user가 맞다면 정상적으로 보여준다.
    return decorated


#

