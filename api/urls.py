


from django.conf.urls import url, include
from django.contrib import admin



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
	url(r'^admin/', admin.site.urls),
        url(r'^', include('large_scale_project.api.urls')),
	url(r'^', include(router.urls)),
]
