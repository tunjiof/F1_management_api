from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .serializers import DriverSerializer
from .models import DriverModel

# Create your views here.
class DriverViews(APIView):
   

    def get(self, request):
        # user_role = request.user.role
        
        drivers = DriverModel.objects.filter(name__icontains= "")
        serializer = DriverSerializer(drivers, many=True)
        return Response({"message": "Drivers get request successful", "drivers": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data_copy = request.data.copy()
        data_copy['user'] = request.user.id
        

        # if user_role != "admin":
        #     return Response({"message": "You must be an admin to create teams."}, status=status.HTTP_403_FORBIDDEN)
        
        
        serializer = DriverSerializer(data=data_copy)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Drivers post request successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, id):
    #     try:
    #         team = TeamModel.objects.get(pk=id)
    #     except TeamModel.DoesNotExist:
    #         return Response({"message": "Data not found."},status=status.HTTP_404_NOT_FOUND)    
        
    #     Serializer = TeamSerializer(team, data=request.data)
    #     if Serializer.is_valid():
    #         Serializer.save()
    #         return Response({"message": "Teams put request successful"}, status=status.HTTP_200_OK)

    #     return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def delete(self, request, id):
    #     try:
    #         team = TeamModel.objects.get(pk=id)
    #     except TeamModel.DoesNotExist:
    #         return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
    #     team.delete()
    #     return Response({"message": "Team data deleted successfully"},status=status.HTTP_204_NO_CONTENT)
