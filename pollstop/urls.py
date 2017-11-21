from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from accounts import views as av
from polls import views as pv
from tags import views as tv

router = routers.SimpleRouter()

router.register(r'users', av.UserViewSet)
router.register(r'auth', av.AuthViewSet)
router.register(r'polls', pv.PollViewSet)
router.register(r'choices', pv.ChoiceViewSet)
router.register(r'tags', tv.TagViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls, namespace='apiv1')),
]
