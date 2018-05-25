from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Promo,PromoPurchase
from rest_framework import status
from member.models import Member


class PromosList(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            promo = Promo.objects.all()
            response = {}
            data_list = []
            for p in promo:
                data = {
                    'code': p.code,
                    'description': p.description,
                    'amount': p.amount,
                    'title': p.title
                }
                data_list.append(data)
            response['status'] = True
            response['data'] = data_list
            return Response(response)
        except Exception as e:
            return Response({'status': False, 'msg': "Error in fetching promos"})


class PromoDetail(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            code = str(request.data.get('pcode'))
            member = str(request.data.get('mem'))
            member = Member.objects.get(name=member)
            promo = Promo.objects.filter(code=code)
            if len(promo) > 0:
                promo = promo[0]
            pp = PromoPurchase.objects.filter(promo=promo, member=member)
            pp = len(pp)
            response = {
                'status': True,
                'qty': pp,
                'code': promo.code,
                'description': promo.description,
                'amount': promo.amount,
                'title': promo.title
            }
            return Response(response)
        except Exception as e:
            return Response({'status': False, 'msg': "Error in fetching promo details"})


class Purchase(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        code = str(request.data.get('pcode'))
        member = str(request.data.get('mem'))
        try:
            promo = Promo.objects.get(code=code)
            member = Member.objects.get(name=member)
            pp = PromoPurchase(promo=promo, member=member)
            pp.save()
            qty = len(PromoPurchase.objects.filter(promo=promo, member=member))
            return Response({'status': True, 'qty': qty})
        except Exception as e:
            return Response({'status': False,
                             'msg': "Error in purchasing promos"})


class Transfer(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        code = str(request.data.get('pcode'))
        member = str(request.data.get('mem'))
        member_to = str(request.data.get('memto'))
        try:
            promo = Promo.objects.get(code=code)
            member = Member.objects.get(name=member)
            member_to = Member.objects.filter(name=member_to)
            if not member_to:
                return Response({'status': False, 'msg': "Member doesnt exist"})
            else:
                member_to = member_to[0]
            pp = PromoPurchase.objects.filter(promo=promo, member=member)
            if pp:
                qty = len(pp)-1
                pp[0].delete()
            else:
                return Response({'status': False, 'msg': "You do not have promos to gift"})
            pp_new = PromoPurchase(promo=promo, member=member_to)
            pp_new.save()
            return Response({'status': True, 'qty': qty})
        except Exception as e:
            return Response({'status': False,
                             'msg': "Error in Gifting promo"})