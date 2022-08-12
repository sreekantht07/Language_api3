from rest_framework.views import APIView
from rest_framework.response import Response
from textblob import TextBlob
from tenseflow import change_tense
class NounFinderAPIViewVersion1(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        if sentance:
            result = TextBlob(sentance.title())
            result = result.noun_phrases
            response["status_code"] = 200
            if result:
                response["nouns"] = result
            else:
                response["nouns"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)

class NounFinderAPIViewVersion2(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        pattern = ["NN","NNS","NNP","NNPS"]
        noun_list = []
        if sentance:
            result = TextBlob(sentance)
            result = result.pos_tags
            if result:
                for item in result:
                    if item[1] in pattern:
                        noun_list.append(item[0])
            if result:
                response["nouns"] = noun_list
            else:
                response["nouns"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)

class PastTenseChangeAPIView(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        if sentance:
            result = change_tense(sentance, "past")
            response["status_code"] = 200
            if result:
                response["past_tense"] = result
            else:
                response["past_tense"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)

class FutureTenseChangeAPIView(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        if sentance:
            result = change_tense(sentance, "future")
            response["status_code"] = 200
            if result:
                response["future_tense"] = result
            else:
                response["future_tense"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)


class PresentTenseChangeAPIView(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        if sentance:
            result = change_tense(sentance, "present")
            response["status_code"] = 200
            if result:
                response["present_tense"] = result
            else:
                response["present_tense"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)


class VerbFinderAPIView(APIView):
    def get(self, request):
        response = {}
        sentance = request.data.get("sentance")
        pattern = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
        verb_list=[]
        if sentance:
            result = TextBlob(sentance)
            result = result.pos_tags
            if result:
                for item in result:
                    if item[1] in pattern:
                        verb_list.append(item[0])
            response["status_code"] = 200
            if result:
                response["verb"] = verb_list
            else:
                response["verb"] = None
        else:
            response["status_code"] = 400
            response["message"] = "please provide valid parameter."
        return Response(response)
