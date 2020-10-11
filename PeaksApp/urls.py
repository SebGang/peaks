from django.urls import path, include
from .views import PeakViewSet, index, peak_list
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('detail', PeakViewSet)


# def print_url_pattern_names(patterns):
#     """Print a list of urlpattern and their names"""
#     for pat in patterns:
#         if pat.__class__.__name__ == 'URLResolver':      # load patterns from this URLResolver
#             print_url_pattern_names(pat.url_patterns)
#         elif pat.__class__.__name__ == 'URLPattern':     # load name from this URLPattern
#             if pat.name is not None:
#                 print('[API-URL] {:>50} -> {}'.format(pat.name, pat.pattern))

# urlpatterns = router.urls
urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls), name='peaks-list'),
    path('<int:id>/', include(router.urls)),
    path('filter/', peak_list, name='peaks-filter')
]

# print_url_pattern_names(urlpatterns)
