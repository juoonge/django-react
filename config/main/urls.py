from urllib.parse import urlparse
from django.urls import URLPattern, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail

urlpatterns=[
    path('review/',ReviewList.as_view()),
    path('review/<int:pk>/',ReviewDetail.as_view()),    
]
urlpatterns=format_suffix_patterns(urlpatterns)

# 웹 API의 일반적 패턴은 URL에서 파일 이름 확장자를 사용하여 특정 미디어임을 알려주는 것이다.
# 예를 들어'http://example.com/api/users.json' 은 JSON표현을 지칭하는 것!
# 그러나 이러한 패턴은 오류가 발생하기 쉽고 DRY원칙에도 어긋난다.
# 따라서 REST framework는 이러한 형식 접미사 패턴을 URLconf에 추가하는 방법을 제공 -> format_suffix_patterns

# format_suffix_patterns(urlpatterns, suffix_required=False, allowed=None) 형태가 기본이며,
# 제공된 각 URL 패턴에 추가된 형식 접미사 패턴을 포함하는 URL 패턴 list를 반환

# ex) urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
# 또한 format_suffix_patterns를 사용하는 경우 'format'키워드 인수를 해당 뷰에 추가해야 한다.
# 그렇구먼! 즉 view에서 사용한 format=None과, urls의 format_suffix_patterns는 세트로 붙어 다니면서
# 파일 형식 접미사를 url에서 어떻게 할 것인가를 결정짓는다고 생각하면 됨
