from django.shortcuts import get_object_or_404, render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import DateDetailView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from .forms import UserForm, ListForm, CardForm, CardCreateFromHomeForm 
from . models import List,Card

from django.views.generic import ListView



# Create your views here.

class HomeView(ListView):
    model = List
    template_name = "kanai_app/web_kanri/kanban_home.html"
    context_object_name = "kanban_home_list"

################## リスト作成用　（新規）　フォーム ##################
# class ListCreateView(LoginRequiredMixin, CreateView):
class ListCreateView(CreateView):
     
     model = List 
     template_name = 'kanai_app/web_kanri/todo_create.html'
     form_class = ListForm
     
     ### 処理終了後　に　TO-DO リスト一覧表示へ　画面遷移
     success_url = reverse_lazy("kanban:home")

     def form_valid(self, form):
          form.instance.user = self.request.user
          return super().form_valid(form)

################ リスト表示　一覧
class ListListView(ListView):
     
     model = List
     template_name = "kanai_app/web_kanri/todo_list.html"
     context_object_name = 'to_do_list'

################ リスト アップデート処理
class ListUpdateView(UpdateView):

     model = List
     template_name = "kanai_app/web_kanri/todo_update.html"
     form_class = ListForm

     def get_success_url(self):
          return resolve_url('kanban:kanban_list')

################ リスト削除
class ListDeleteView(DeleteView):

     model = List
     template_name = "kanai_app/web_kanri/todo_delete.html"
     context_object_name = "to_do_delete_list"

     success_url = reverse_lazy("kanban:home")


########################## Card 新規作成
##########################
class CardCreateView(CreateView):

     model = Card
     template_name = "kanai_app/web_kanri/card_create.html"
     form_class = CardForm
     success_url = reverse_lazy("kanban:home")

     def form_valid(self, form):
          form.instance.user = self.request.user
          return super().form_valid(form)

########################## Card 一覧表示
class CardListView(ListView):

     model = Card
     template_name = "kanai_app/web_kanri/card_listview.html"
     context_object_name = "card_list"

########################## Card 詳細
class CardDetailView(DetailView):

     model = Card
     template_name = "kanai_app/web_kanri/card_detail.html"
     context_object_name = "card_detail_list"


########################## Card 削除処理
class CardDeleteView(DeleteView):

     model = Card
     template_name = "kanai_app/web_kanri/card_delete.html"
     context_object_name = "card_delete_list"
     
     success_url = reverse_lazy("kanban:home")

########################### Card 更新処理
class CardUpdateView(UpdateView):

     model = Card
     template_name = "kanai_app/web_kanri/card_update.html"
     form_class = CardForm

     def get_success_url(self):
          return resolve_url('kanban:card_detail', pk=self.kwargs['pk'])


##################################### フォームの外部キーに　デフォルトで　値を入れる
class CardCreateFromHomeView(CreateView):
     
     model = Card
     template_name = "kanai_app/web_kanri/card_create.html"
     form_class = CardCreateFromHomeForm ### 追加した　フォームを使う 
     success_url = reverse_lazy("kanban:home")

     def form_valid(self, form):
          list_pk = self.kwargs['list_pk']
          list_instance = get_object_or_404(List, pk=list_pk)

          form.instance.list = list_instance
          form.instance.user = self.request.user

          return super().form_valid(form)









     
