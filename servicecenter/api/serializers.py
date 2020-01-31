from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from center.models import UserProfile

class UserCreateSerilizer(ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ["username","password","phone","address"]
	def validate_phone(self, value):
		if len(value)!=10:
			raise serializers.ValidationError("phone number not valid")
		return value
	def validate_username(self, value):
		# write user name validations
		return value
class UserGetSerializer(ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ["username","phone","address"]
