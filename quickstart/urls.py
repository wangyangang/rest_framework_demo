from django.urls import path, include
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

#urlpatterns = [
    #path('', views.api_root),

    # path('quickstart/', views.snippet_list),
    #path('snippets/', views.SnippetListView3.as_view(), name='snippet-list'),
    # path('quickstart/<int:pk>/', views.snippet_detail),
    #path('snippets/<int:pk>/', views.SnippetDetailView3.as_view(), name='snippet-detail'),

    #path('users/', views.UserListView.as_view(), name='user-list'),
    #path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    #path('snippets/<int:pk>/highlight/', views.SnippetHighlightView.as_view(), name='snippet-highlight'),
#]
#urlpatterns = format_suffix_patterns(urlpatterns) # 改造url，使其支持后缀