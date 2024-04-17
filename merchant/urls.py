from django.urls import path

from merchant.api import views as api_views

urlpatterns = [
    path("merchant/application", api_views.ApplicationAPIAPIView.as_view(), name="create_application"),
    path("merchant/channel", api_views.ChannelAPIAPIView.as_view(), name="create_channel")
]
