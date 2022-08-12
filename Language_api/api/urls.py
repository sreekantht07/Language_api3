from django.urls import path
from .views import NounFinderAPIViewVersion1,NounFinderAPIViewVersion2, PastTenseChangeAPIView, FutureTenseChangeAPIView, PresentTenseChangeAPIView,VerbFinderAPIView


urlpatterns = [
    path('nounfinder1', NounFinderAPIViewVersion1.as_view()),
    path('nounfinder2', NounFinderAPIViewVersion2.as_view()),
    path('past_tense_changer', PastTenseChangeAPIView.as_view()),
    path('future_tense_changer', FutureTenseChangeAPIView.as_view()),
    path('present_tense_changer', PresentTenseChangeAPIView.as_view()),
    path('verbfinder2', VerbFinderAPIView.as_view())

    ]