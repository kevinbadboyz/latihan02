from django.urls import path, include
# from .views import (
#     StatusModelList, StatusModelCreate, StatusModelUpdate, StatusModelDetail,
#     TransactionDetail, 
#     ItemList, ItemCreate, ItemUpdate, ItemDetail,
# )
from web_app import views
app_name = 'web_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('login', views.login_account, name = 'login'),
    # path('register/admin', views.register_admin, name = 'register_admin'),
    # path('register/scale', views.register_scale, name = 'register_scale'),
    # path('logout', views.logout_account, name = 'logout'),
    # path('change-password', views.change_password, name = 'change_password'),
    # path('profile-info', views.profile_info, name = 'profile_info'),
    # path('profile-update', views.profile_update, name = 'profile_update'),
    # path('account-admin-list', views.account_admin_list, name = 'account_admin_list'),
    # path('account-scale-list', views.account_scale_list, name = 'account_scale_list'),
    # path('status-model-list', StatusModelList.as_view(), name = 'status_model_list'),
    path('status-model-list', views.status_model_list, name = 'status_model_list'),
    # path('status-model-create', StatusModelCreate.as_view(), name = 'status_model_create'),
    # path('status-model-update/<pk>', StatusModelUpdate.as_view(), name = 'status_model_update'),
    # path('status-model-info/<pk>', StatusModelDetail.as_view(), name = 'status_model_info'),
    # path('transaction-scale-upload', views.transaction_scale_upload, name = 'transaction_scale_upload'),
    # path('transaction-scale-list', views.transaction_scale_list, name = 'transaction_scale_list'),   
    # path('transaction-scale-info//<pk>', TransactionDetail.as_view(), name = 'transaction_scale_detail'),
    # path('item-list', ItemList.as_view(), name = 'item_list'),
    # path('item-create', ItemCreate.as_view(), name = 'item_create'),
    # path('item-update/<pk>', ItemUpdate.as_view(), name = 'item_update'),
    # path('item-info/<pk>', ItemDetail.as_view(), name = 'item_info'),
    # path('about-program', views.about_program, name = 'about_program'),   
]