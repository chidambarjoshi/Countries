from django.http.response import JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from .models import Image
from .serializers import ImageSerializer
import mysql.connector
from countries.settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
import boto3
from boto3.s3.transfer import TransferConfig
import base64

# Set the desired multipart threshold value (5GB)
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)

s3 = boto3.resource('s3')



#Using coustom querries with viewsets



class CountriesViewSet(viewsets.ViewSet):    
    def state(self,request):
        '''
        Api to fetch State list in from {id:state} based on country_id
        '''
        cnx = mysql.connector.connect(user='mysqluser', password="X-Nd>)w9;4n4}xYP", host='142.93.214.61', database='mysqldb')
        cursor = cnx.cursor()
            
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
    authentication_classes=BasicAuthentication
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
        s3_client = boto3.client('s3',region_name='us-east-1', 
                  aws_access_key_id=AWS_ACCESS_KEY_ID, 
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        bucket_response = s3_client.list_buckets()
        buckets = bucket_response["Buckets"]
        print()
        
        
        try:
            print('try')
            response =s3.meta.client.upload_file(video,buckets[0]['Name'],'video/{}'.format(video))
            print('try')
            print(response)
        except Exception as e:
            logging.error(e)
            print(e)
            return JsonResponse({},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({},status=status.HTTP_201_CREATED)
        

