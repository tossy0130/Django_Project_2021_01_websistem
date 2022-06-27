from django.urls import path
from . import views

app_name = "kanban"

urlpatterns = [

    path('home/', views.HomeView.as_view(), name="home"), # 追加

    path('', views.ListCreateView.as_view(), name="kanban_create"),

    path('list/', views.ListListView.as_view(), name="kanban_list"),

    ### T0-Do 更新
    path('list/<int:pk>/update/', views.ListUpdateView.as_view(), name="kanban_update"),
    
    ### To-Do 削除
    path('list/<int:pk>/delete/', views.ListDeleteView.as_view(), name="kanban_delete"),

    ### Card 作成
    path('cards/create/', views.CardCreateView.as_view(), name="card_create"),
    path('cards/list/', views.CardListView.as_view(), name="card_list"),
    path('cards/<int:pk>/', views.CardDetailView.as_view(), name="card_detail"),
    # 削除
    path('cards/<int:pk>/delete/', views.CardDeleteView.as_view(), name="card_delete"),
    # 更新
    path('cards/<int:pk>/update/', views.CardUpdateView.as_view(), name="card_update"),

    ### 新規作成　プライマリキー　最初から　入力ビュー
    path("cards/create/<int:list_pk>", views.CardCreateFromHomeView.as_view(), name="cards_create_from_home"),

]