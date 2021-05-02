
# # @api_view(['GET','POST'])
# # def cityList(request):
# #     '''API to fetch all cities and fetch details of particular city and add new city details
# #        Author : Chidambar Joshi
# #        API:  http://127.0.0.1:8000/api/city
# #        POST: 
# #             Body: {
# #                     "city": "Belgaum",
# #                     "state": "AP",
# #                     "country": "India"
# #                   }
# #       GET: 

# #             To get particular city details
# #             url: http://127.0.0.1:8000/api/city/?city='<city_name>'

# #             To get all city details
# #             url:http://127.0.0.1:8000/api/city/


# #      '''
# #     if request.method == 'GET':
        
        
# #         city=request.GET.get('city',None)
# #         if city :
# #             try:
# #                 cities=City.objects.filter(city__icontains=city)
# #             except:
# #                 return JsonResponse({'message':'The City Does Not exists'}, status=status.HTTP_400_BAD_REQUEST)              
# #         else:
# #             cities=City.objects.all()
# #         city_serializer=CitySerializer(cities,many=True)
# #         return JsonResponse(city_serializer.data,safe=False)


# #     elif request.method=="POST":
# #         city_data= JSONParser().parse(request)
        
# #         if City.objects.filter(city=city_data['city'],state=city_data['state']).exists():
# #              return JsonResponse({'message':'The City already exists'}, status=status.HTTP_400_BAD_REQUEST) 

# #         city_serializer=CitySerializer(data=city_data)
# #         if city_serializer.is_valid():
# #             city_serializer.save()
# #             return JsonResponse(city_serializer.data,status=status.HTTP_201_CREATED)
# #         return JsonResponse(city_serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# # @api_view(['GET','PUT','DELETE'])
# # def city_detail(request,username):
# #     '''API to update and delete city details 
# #        Author : Chidambar Joshi
# #        API : 
# #      '''
# #     try:
# #         cities=City.objects.get(city=username)
# #     except City.DoesNotExist:
# #         return JsonResponse({'message':'The City Does Not exists'}, status=status.HTTP_404_NOT_FOUND)
    
# #     if request.method == 'GET':
# #         city_serializer= CitySerializer(cities)
# #         return JsonResponse(city_serializer.data)
    
# #     elif request.method == 'PUT':
# #         cities_data=JSONParser().parse(request)
# #         city_serializer=CitySerializer(cities,data=cities_data)
# #         if city_serializer.is_valid():
# #             city_serializer.save()
# #             return JsonResponse(city_serializer.data)
# #         return JsonResponse(city_serializer.errors , status=status.HTTP_400_BAD_REQUEST)




# #     elif request.method == 'DELETE':
# #         cities.delete()
# #         return JsonResponse({'message':'City Deleted SuccessFully!'}, status=status.HTTP_204_NO_CONTENT)

# # @api_view(['GET','PUT','DELETE'])
# # def city_test(request):
# #     if request.method == 'GET':
# #         return JsonResponse(JsonResponse)


# from django.http.response import JsonResponse
# from rest_framework import status
# from rest_framework import viewsets
# import mysql.connector
# import math



# #Using coustom querries with viewsets

# cnx = mysql.connector.connect(user='mysqluser', password="X-Nd>)w9;4n4}xYP", host='142.93.214.61', database='mysqldb')
# cursor = cnx.cursor()

# class CountriesViewSet(viewsets.ViewSet):
#     def country(self,request):
#         '''
#             Api to fetch list  countries in from {id:country} 

#         '''
#         query="Select name,id from countries"
#         cursor.execute(query)
#         country=cursor.fetchall()
#         ctr_list=dict((y, x) for x, y in country)
        
#         return JsonResponse(ctr_list, status=status.HTTP_204_NO_CONTENT)
    
#     def state(self,request,pgno):
#         '''
#         Api to fetch State list in from {id:state} based on country_id
#         '''
#         cursor.execute("SELECT COUNT(*) from states ")
#         (number_of_rows,)=cursor.fetchone()
        
#         totalpages=math.ceil(number_of_rows/50)
#         currentpage=int(pgno)
#         offsetvalue=(int(pgno)-1)*50
#         states={}
        
#         query="select name,id from states order by name LIMIT 50 OFFSET {0} ".format(offsetvalue)
#         print(query)
#         cursor.execute(query)
#         state=cursor.fetchall()
#         info={'page':currentpage,
#                     'total':totalpages,
#                     'No state':len(state)}
#         states.update(info)
        
       
#         for state1,id in state:
            
#             query="select name,id from cities where state_id={0} order by name".format(id)
#             cursor.execute(query)
#             city=cursor.fetchall()
            
#             city_list=list(x for x, y in city)
#             states.update({state1:city_list})
        
            
        
#         return JsonResponse(states)
#     def state(self,request,pgno):
#         '''
#         Api to fetch State list in from {id:state} based on country_id
#         '''
#         cursor.execute("SELECT COUNT(*) from states ")
#         (number_of_rows,)=cursor.fetchone()        
#         totalpages=math.ceil(number_of_rows/50)
#         currentpage=int(pgno)
#         offsetvalue=(int(pgno)-1)*50
#         states={}        
#         query="select name,id from states order by name LIMIT 50 OFFSET {0} ".format(offsetvalue)
#         print(query)
#         cursor.execute(query)
#         state=cursor.fetchall()
#         info={'page':currentpage,
#                     'total':totalpages,
#                     'No state':len(state)}
#         states.update(info)       
       
#         for state1,id in state:
#             query="select name,id from cities where state_id={0} order by name".format(id)
#             cursor.execute(query)
#             city=cursor.fetchall()            
#             city_list=list(x for x, y in city)
#             if len(city_list)== 0:
#                 city_list=[state1]
#             states.update({state1:city_list})
        
#         return JsonResponse(states)
   




# #URLS


# # url(r'^api/city$',views.cityList),
#     # url(r'^api/city_byname/(?P<username>\w{0,50})/$',views.city_detail),
#     #  url(r'^api/country/',views.CountriesViewSet.as_view({'get': 'country'})),
#     # url(r'^api/state/(?P<pk>[0-9]+)/$',views.CountriesViewSet.as_view({'get': 'state'})),
#     # url(r'^api/city/(?P<pk>[0-9]+)/$',views.CountriesViewSet.as_view({'get': 'city'}))

#      #   url(r'^api/city/$',views.CountriesViewSet.as_view({'get': 'city'}))
