from django.conf.urls import url
from .member_info_api import *
urlpatterns = [
    url(r"^member$", MemberInfoViewSet.as_view({"post": "member_register"})),
    url(r"^info_manage$", MemberInfoAPIView.as_view()),
    url(r"^delete_member$", EditMemberInfo.as_view({"post": "delete"})),
    url(r"^update_info$", UpdateMemberInfo.as_view()),
    url(r"^search$", SearchMemberAPIView.as_view()),
    url(r"^again_card", MemberContinuityCard.as_view({"post": "again"})),
]