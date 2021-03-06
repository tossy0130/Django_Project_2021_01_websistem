from django.db import models

# Create your models here.

####### ユーザー作成用　、ログイン、ログアウト
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
####### ユーザー作成用　、ログイン、ログアウト END

from django.urls import reverse_lazy,reverse

############ 取扱商品　カテゴリー テーブル （取扱商品ページ用） ############
class Toriatukai_Cate(models.Model):

    # 取扱品　コード
    Toriatukai_code = models.IntegerField('取扱商品コード（WEB表示用）',blank=False, null=False, unique=True, default=0)

    # 取扱品　タイトル
    Toriatukai_title = models.CharField('取扱商品 タイトル（WEB表示用）', max_length=50, blank=False, null=False,default='')

    def __str__(self):
        return '{0}:{1}'.format(self.Toriatukai_code, self.Toriatukai_title)

    ########## リダイレクト用 ############
    def get_absolute_url(self):
        return reverse('kanai_app:kanri_top', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '取扱カテゴリー登録'
        verbose_name_plural = '取扱カテゴリー登録'

############ 取扱商品　カテゴリー テーブル END ############

############ 中カテゴリー　Medium_category ############
class Medium_category(models.Model):

    # （中）品名カテゴリー  コード
    Medium_code = models.IntegerField('品名カテゴリーコード', blank=False, null=False, unique=True)

    # （中）品名カテゴリー　タイトル
    Medium_title = models.CharField('品名カテゴリータイトル', max_length=100,blank=False, null=False)

    # 画像サムネイル用
     ################ 画像ファイル追加
    Medium_image = models.ImageField(upload_to="images/uploaded/category_01/", default=None, null=True, blank=True)

    ######## 外部キー設定
    M_Toriatukai_code = models.ForeignKey(Toriatukai_Cate, verbose_name='取扱品コード',
                                on_delete=models.CASCADE, null=False, blank=False,
                                db_column='M_Toriatukai_code', to_field='Toriatukai_code')

    ######### キー 補助 null , blank 大丈夫
    M_code = models.IntegerField('上記で選択した番号を入力してください。',blank=True, null=True)

    def __str__(self):
        return '{0}：{1}'.format(self.Medium_code, self.Medium_title)

    class Meta:
        verbose_name = '品名カテゴリー'
        verbose_name_plural = '品名カテゴリー'

############ 中カテゴリー　Medium_category END ############ 


#################  テスト商品データ登録　01  Ttable
class Test_shouhin_010(models.Model):

    # メーカーコード
    Test_shouhin_010_code = models.CharField('メーカーコード', max_length=50, null=False, blank=False)
    # メーカー名
    Test_shouhin_010_name = models.CharField('メーカー名', max_length=50, null=False, blank=False)
    # 商品名
    Test_shouhin_010_str = models.CharField('商品名', max_length=100, null=False, blank=False)

    # メーカー小カテゴリー ****** 1 = フック用シール , 2 = フック
    Test_shouhin_010_code_02 = models.CharField('メーカー小カテゴリーコード',max_length=100, null=True, blank=True)

    # メーカー小カテゴリー名 ****** (例) フック用シール,  フック
    Test_shouhin_010_name_02 = models.CharField('メーカー小カテゴリーコード',max_length=100, null=True, blank=True)

    # サムネイル画像
    Test_shouhin_010_image = models.ImageField(upload_to='images/uploaded/shouhin/', 
    default=None, null=True,blank=True)

    # 商品カテゴリーコード　外部キー
    T_Medium_code_02 = models.ForeignKey(Medium_category, verbose_name='品名カテゴリー',
                                    on_delete=models.CASCADE, null=False, blank=False,
                                    db_column='T_Medium_code', to_field='Medium_code')


    ################# 05/13 追加　カラム #################

    # JANコード
    jan_code = models.IntegerField('JANコード', null=False, blank=False, default=0)

    # カウンター
    counter = models.CharField('カウンター', null=False, blank=False, max_length=50, default='')

    # 検索用品名
    search_hinmei = models.CharField('検索用品名', null=True, blank=True, max_length=150, default='')

    # 商品説明
    description_item = models.TextField('商品説明', null=True, blank=True, max_length=255, default='')

    # 規格
    kikaku  = models.CharField('検索用品名', null=False, blank=False, max_length=50, default='')

    # 仕様名称 01
    siyou_name_01 = models.CharField('仕様名称 01', null=True, blank=True, max_length=150, default='')
    # 仕様内容 01
    siyou_content_01 = models.TextField('仕様内容 01', null=True, blank=True, max_length=255, default='')

    # 仕様名称 02
    siyou_name_02 = models.CharField('仕様名称 02', null=True, blank=True, max_length=150, default='')
    # 仕様内容 02
    siyou_content_02 = models.TextField('仕様内容 02', null=True, blank=True, max_length=255, default='')

    # 仕様名称 03
    siyou_name_03 = models.CharField('仕様名称 03', null=True, blank=True, max_length=150, default='')
    # 仕様内容 03
    siyou_content_03 = models.TextField('仕様内容 03', null=True, blank=True, max_length=255, default='')

    # 仕様名称 04
    siyou_name_04 = models.CharField('仕様名称 04', null=True, blank=True, max_length=150, default='')
    # 仕様内容 04
    siyou_content_04 = models.TextField('仕様内容 04', null=True, blank=True, max_length=255, default='')

    # 仕様名称 05
    siyou_name_05 = models.CharField('仕様名称 05', null=True, blank=True, max_length=150, default='')
    # 仕様内容 05
    siyou_content_05 = models.TextField('仕様内容 05', null=True, blank=True, max_length=255, default='')
    
    # 廃盤 F
    haiban_flg = models.IntegerField('廃盤 F', null=True, blank=True, default=0)

     # サムネイル画像 02
    sh_thumbnail_02 = models.ImageField(upload_to='images/uploaded/shouhin/', 
    default=None, null=True,blank=True)

     # サムネイル画像 03
    sh_thumbnail_03 = models.ImageField(upload_to='images/uploaded/shouhin/', 
    default=None, null=True,blank=True)

    ################# オリジナル商品 & おすすめ商品
    ORIGINARU_S = ((0, '通常商品'), (1,'オリジナル商品'), (2,'おすすめ商品'))
    
    # 商品判別 Flg
    shouhin_flg = models.IntegerField(verbose_name='商品選別 フラグ',choices=ORIGINARU_S, default=0)
 

    def __str__(self):
        return '{0}, {1}'.format(self.Test_shouhin_010_code, self.Test_shouhin_010_name)

    class Meta:
        verbose_name = 'テスト商品登録01'
        verbose_name_plural = 'テスト商品登録01'


######################## トップページ　スライダー表示　テーブル
class Product(models.Model):
    class Meta:
        verbose_name = 'スライダー画像'
        verbose_name_plural = 'スライダー画像'

    thumbnail = models.ImageField(
        verbose_name = 'サムネイル',
        # アップロード先
        upload_to = "images/uploaded/top_slide/",
        null=True,
        blank=True
    )

    name = models.CharField(
        verbose_name = 'スライダー名',
        max_length=30,
        null=True,
        blank=True,
		default='',
    )

    price = models.IntegerField(
        verbose_name = '価格',
        null=True,
        blank=True,
		default=0,
    )

    description = models.TextField(
        verbose_name = '説明',
        null=True,
        blank=True,
		default='',
    )


################## テスト商品データ　01 CSV 取込み用 Test_shouhin_01
class Test_shouhin_01(models.Model):

    # メーカーコード
    Test_shouhin_01_code = models.CharField(verbose_name='メーカーコード', max_length=50, null=False, blank=False,default='')
    # メーカー名
    Test_shouhin_01_name = models.CharField(verbose_name='メーカー名', max_length=50, null=False, blank=False,default='')
    # 商品名
    Test_shouhin_01_str = models.CharField(verbose_name='商品名', max_length=100, null=True, blank=False,default='')

    # サムネイル画像
    Test_shouhin_01_image = models.ImageField(upload_to='images/img_test_01/', 
    default=None, null=True,blank=True)

    class Meta:
        verbose_name = 'テスト商品登録01'
        verbose_name_plural = 'テスト商品登録01'


#################### オリジナル商品
class Original_Cate(models.Model):

    ### オリジナル カテゴリー　コード
    original_cate_code = models.IntegerField(verbose_name='オリジナルカテゴリーコード')

    ### オリジナル カテゴリー　名
    original_cate_name = models.CharField(verbose_name='オリジナルカテゴリー名',max_length=100,
                        null=True, blank=True, default='')

    ### オリジナルカテゴリー　サムネイル
    original_cate_thumbnail = models.ImageField(upload_to='images/uploaded/category_original/',
                        default=None, null=True, blank=True)
    

    def __str__(self):
        return self.name

##################### TOP index ニュース記事　エリア
class Post(models.Model):

    new_title = models.CharField(verbose_name='新着タイトル', max_length=100, null=True, blank=False,default='')

    text = models.TextField(verbose_name='新着ニュース',blank=False, null=True,default='')

###################### メーカーコード　Table ######################
class Maker_master(models.Model):

   # メーカーコード  
   maker_code = models.IntegerField(verbose_name='メーカーコード', primary_key=True, null=False, blank=False,default=0)
   
   # メーカー名
   maker_name = models.CharField(verbose_name='メーカー名', max_length=40, null=False, blank=False,default='')
   # 販売店
   hanbaiten =  models.CharField(verbose_name='販売店', max_length=40, null=False, blank=True,default='')
   # URL
   maker_code_url = models.CharField(verbose_name='URL', max_length=200, null=False, blank=True,default='')
   # キーワード
   web_maker_keyword = models.CharField(verbose_name='キーワード', max_length=200, null=False, blank=True,default='')

   def __str__(self):
         return str(self.maker_code)

   class Meta:
          verbose_name = 'メーカーコード登録'
          verbose_name_plural = 'メーカーコード登録'

###################### ブランドコード　Table ######################
class Brand_master(models.Model):
    
    # メーカーコード 外部キー
    b_maker_code = models.ForeignKey(Maker_master, verbose_name='メーカーコード',
                                    on_delete=models.CASCADE, null=False, blank=False,
                                    db_column='b_maker_code', to_field='maker_code')

    # ブランドコード
    brand_code = models.IntegerField(verbose_name='ブランドコード', null=False, blank=False,default=0)
    # ブランド名
    brand_name = models.CharField(verbose_name='ブランド名', max_length=40, null=False, blank=False,default='')
    # キーワード
    web_brand_keyword = models.CharField(verbose_name='キーワード',max_length=200, null=False, blank=True,default='')

    def __str__(self):
             return self.brand_code

    class Meta:
            verbose_name = 'ブランド登録'
            verbose_name_plural = 'ブランド登録'


###################### 代理店　Table ######################
class Agency_master(models.Model):

    # メーカーコード 外部キー
    a_maker_code = models.ForeignKey(Maker_master, verbose_name='メーカーコード',
                                    on_delete=models.CASCADE, null=False, blank=False,
                                    db_column='a_maker_code', to_field='maker_code')

    # 代理店コード
    agency_code = models.IntegerField(verbose_name='代理店コード', null=False, blank=False,default=0)
    # 代理店名
    agency_name = models.CharField(verbose_name='代理店名', max_length=40, null=False, blank=False,default='')
    # キーワード
    web_agency_keyword =  models.CharField(verbose_name='キーワード',max_length=200, null=False, blank=True)

    def __str__(self):
             return self.brand_code

    class Meta:
            verbose_name = '代理店登録'
            verbose_name_plural = '代理店登録'


###################### QR コード　作成テーブル　Table ######################
class Jan_QR(models.Model):

   cr_jan_01 = models.IntegerField('janコード生成', blank=True, null=True)

   cr_qr_01 = models.CharField('QRコード生成', blank=True, null=True, max_length=255)

   def __str__(self):
       return '{0}, {1}'.format(self.cr_jan_01, self.cr_qr_01)

   class Meta:
        verbose_name = 'JANコード, QRコード生成'
        verbose_name_plural = 'JANコード, QRコード生成'

        
