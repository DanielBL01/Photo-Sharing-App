from django.urls import path

from .views import homePageView, createNewPost, deleteUserPost, updateUserPost, createComment, infoPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('post/new/', createNewPost, name = 'post_new'),

    path('post/<int:pk>/delete/', deleteUserPost, name = 'post_delete'),
    path('post/<int:pk>/update/', updateUserPost, name = 'post_update'),
    path('post/<int:pk>/comments/', createComment, name = 'post_comment'),

    path('info_page/', infoPageView, name = 'info')
]
