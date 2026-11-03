from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View


class HotelView(View):
    def get(self, request):
        data = {
            "hotel_name": "Grand Palace",
            "location": "Kochi",
            "contact": "9876543210",
            "rating": 5,
            "status": "Open"
        }
        return JsonResponse(data)


class RoomView(View):
    def get(self, request):
        data = {
            "room_number": 101,
            "room_type": "Deluxe",
            "price": 2500,
            "availability": "Available"
        }
        return JsonResponse(data)


class CustomerView(View):
    def get(self, request):
        data = {
            "id": 1,
            "name": "Anu",
            "place": "Thrissur",
            "mobile": 9876543210,
            "booking_status": "Confirmed"
        }
        return JsonResponse(data)


class ServicesView(View):
    def get(self, request):
        data = {
            "services": [
                "Room Service",
                "Restaurant",
                "Swimming Pool",
                "Parking",
                "WiFi"
            ]
        }
        return JsonResponse(data)