from rest_framework.pagination import PageNumberPagination

class MyPagenumberPaginatioon(PageNumberPagination):
    page_size = 1 #每页多少个
    max_page_size = 2
    page_size_query_param = 'size'  #关键字
    page_query_param = 'page'
