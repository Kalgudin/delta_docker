from django.contrib import admin
from django.urls import path, include

# from delta_web.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delta.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
]


# if DEBUG:
#     import debug_toolbar
#     urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))



