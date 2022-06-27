## 以下新規作成
################# ログインフォーム　作成
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import fields
from .models import *
from django.core.exceptions import ValidationError

### サマーノート用
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

################ 取扱カテゴリー　追加　フォーム Toriatukai_Cate
class Toriatukai_CateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Toriatukai_Cate
        fields = ('Toriatukai_code','Toriatukai_title')
 
        labels = {
            'Toriatukai_code' : '取扱商品 分類コード（WEB表示用　大カテゴリー）',
            'Toriatukai_title': '取扱分類　タイトル（WEB表示用　大カテゴリー）'
        }

        help_texts  = {
            'Toriatukai_code' : '大分類のコードを入力してください。',
            'Toriatukai_title' : '（例）墜落制止用器具関係(ハーネス、ランヤード、安全帯関係)'
        }

############### 中カテゴリー用　登録フォーム  Medium_category
class Medium_categoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = Medium_category
        fields = ('Medium_code', 'Medium_title','Medium_image','M_Toriatukai_code','M_code')

        labels = {
            'Medium_code' : '中カテゴリー 分類コード（WEB表示用　中カテゴリー）',
            'Medium_title': '分類 タイトル名',
            'Medium_image': '分類サムネイル画像',
            'M_Toriatukai_code': '親の大カテゴリー選択',
            'M_code': '選択した、親の大カテゴリーを再度入力してください'
        }

############## テスト商品 01 Table の Form
class Test_shouhin_010Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = Test_shouhin_010

        fields = ('Test_shouhin_010_code','Test_shouhin_010_name', 'Test_shouhin_010_str',
        'Test_shouhin_010_code_02','Test_shouhin_010_name_02',
        'Test_shouhin_010_image','T_Medium_code_02',
        'jan_code', 'counter', 'search_hinmei', 'description_item', 'kikaku',
        'siyou_name_01', 'siyou_content_01', 'siyou_name_02', 'siyou_content_02',
        'siyou_name_03', 'siyou_content_03', 'siyou_name_04', 'siyou_content_04', 
        'siyou_content_04', 'siyou_name_05', 'siyou_content_05',
        'haiban_flg', 'sh_thumbnail_02','sh_thumbnail_03','shouhin_flg'
        )

        labels = {
            'Test_shouhin_010_code':'メーカーコード',
            'Test_shouhin_010_name':'メーカー名',
            'Test_shouhin_010_str':'商品名',
            'Test_shouhin_010_code_02':'メーカー小カテゴリー',
            'Test_shouhin_010_name_02':'メーカー小カテゴリー名',
            'T_Medium_code_02':'商品カテゴリーコード（選択）',
            'jan_code' : 'JAN コード',
            'counter' : 'カウンター',
            'search_hinmei' : '検索用品名',
            'description_item' : '商品説明',
            'kikaku' : '規格',
            'siyou_name_01' : '仕様名称 01',
            'siyou_content_01' : '仕様内容 01',
            'siyou_name_02' : '仕様名称 02',
            'siyou_content_02' : '仕様内容 02',
            'siyou_name_03' : '仕様名称 03',
            'siyou_content_03' : '仕様内容 03',
            'siyou_name_04' : '仕様名称 04',
            'siyou_content_04' : '仕様内容 04',
            'siyou_name_05' : '仕様名称 05',
            'siyou_content_05' : '仕様内容 05',
            'haiban_flg': '廃盤 Flg',
            'sh_thumbnail_02': '商品サムネイル画像 02', 
            'sh_thumbnail_03': '商品サムネイル画像 03',
            'shouhin_flg': '商品判別 Flg'
        }


############## オリジナル商品カテゴリー　フォーム
class Original_CateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        
        model = Original_Cate

        fields = ('original_cate_code','original_cate_name','original_cate_thumbnail')

        labels = {
            'original_cate_code': 'オリジナルカテゴリー　コード',
            'original_cate_name': 'オリジナルカテゴリー　名',
            'original_cate_thumbnail': 'オリジナルカテゴリー　サムネイル'
        }

############## 新着情報　TOP 登録フォーム
class Post_newForm(forms.ModelForm):

         def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label

         class Meta:

            model = Post

            fields = ('new_title', 'text')

            widgets = {
                'text': SummernoteWidget(),
            }

            labels = {
                'new_title': '新着タイトル',
                'text' : '新着情報'
            }

################ メーカー登録　フォーム
class Maker_master_Form(forms.ModelForm):

          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                for field in self.fields.values():
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label

          class Meta:

              model = Maker_master

              fields = ("maker_code","maker_name","hanbaiten","maker_code_url","web_maker_keyword")
              
              labels = {
                'maker_code': 'メーカーコード',
                'maker_name' : 'メーカー名',
                'hanbaiten': '販売店',
                'maker_code_url': 'URL',
                'web_maker_keyword' : 'キーワード'
              }


################ メーカー登録　フォーム
class Brand_master_Form(forms.ModelForm):

          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                for field in self.fields.values():
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label

          class Meta:

              model = Brand_master

              fields = ("b_maker_code","brand_code","brand_name","web_brand_keyword")
              
              labels = {
                'b_maker_code': 'メーカーコード',
                'brand_code' : 'ブランドコード',
                'brand_name': 'ブランド名',
                'web_brand_keyword': 'キーワード'
              }


################ メーカー登録　フォーム
class Agency_master_Form(forms.ModelForm):

          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                for field in self.fields.values():
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label

          class Meta:

              model = Agency_master

              fields = ("a_maker_code","agency_code","agency_name","web_agency_keyword")
              
              labels = {
                'a_maker_code': 'メーカーコード',
                'agency_code' : '代理店コード',
                'agency_name': '代理店名',
                'web_agency_keyword': 'キーワード'
              }



        
    

       







