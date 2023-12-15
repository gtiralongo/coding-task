from django.contrib import admin
from django.urls import path , include

from .router import router


from .views import      TaskListView   \
                    ,   TaskDetailView \
                    ,   TaskCreateView \
                    ,   TaskUpdateView \
                    ,   TaskDeleteView

app_name = "task"

urlpatterns = [
    path("", TaskListView.as_view(), name="all"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", TaskDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete")
]

urlpatterns += router.urls