from django.http.response import JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
import mysql.connector

import boto3

s3 = boto3.resource('s3')



#Using coustom querries with viewsets

cnx = mysql.connector.connect(user='mysqluser', password="X-Nd>)w9;4n4}xYP", host='142.93.214.61', database='mysqldb')
cursor = cnx.cursor()

class CountriesViewSet(viewsets.ViewSet):    
    def state(self,request):
        '''
        Api to fetch State list in from {id:state} based on country_id
        '''    
        states={}        
        query="select name,id from states where country_id=101 order by name"
        print(query)
        cursor.execute(query)
        state=cursor.fetchall()    
        for state1,id in state:
            query="select name,id from cities where state_id={0} order by name".format(id)
            cursor.execute(query)
            city=cursor.fetchall()            
            city_list=list(x for x, y in city)
            if len(city_list)== 0:
                city_list=[state1]
            states.update({state1:city_list})
        return JsonResponse(states)


def modify_input_for_multiple_files(image_name, image):
    dict = {}
    
    dict['image'] = image
    dict['image_name'] = image_name
    print(dict)
    return dict

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        all_images = Image.objects.all()
        if all_images:
             serializer = ImageSerializer(all_images, many=True ,context={'request':request})
             return JsonResponse(serializer.data, safe=False)
        else :
            data={"message":"No image Found"}
            return JsonResponse(data, safe=False,status=status.status.HTTP_404_NOT_FOUND)

        

    def post(self, request, *args, **kwargs):
        image_name = request.data['image_name']
        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(image_name,img_name)
            file_serializer = ImageSerializer(data=modified_data,context={'request':request})
            if file_serializer.is_valid():
                
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                print(file_serializer.errors)
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)
import logging
import boto3
from botocore.exceptions import ClientError
class videoview(viewsets.ViewSet):
    def list(self,request):
        print("hit")
        bucket = s3.Bucket('xubbabucket')
        
        for key in bucket.objects.all():
            print(key.key)
        
        return JsonResponse({},status=status.HTTP_200_OK)
        
    def videoup(self,request):
        
        video = request.data['video']
        print(request.data)
        s3_client = boto3.client('s3')
        print(video)
        
        try:
            print('try')
            response =s3_client.upload_file(video, 'xubbabucket','video/{}'.format(video))# s3_client.upload_file(video, 'xubbabucket','video/{}'.format(video))
            print(response)
        except ClientError as e:
            logging.error(e)
            print(e)
            return JsonResponse({},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({},status=status.HTTP_201_CREATED)
        

