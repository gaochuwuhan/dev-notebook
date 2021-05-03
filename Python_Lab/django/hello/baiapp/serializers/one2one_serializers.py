from baiapp.models import Account,Contact
from rest_framework import serializers


class AccountSerializers(serializers.ModelSerializer):

    # tel=serializers.CharField(source='contact_account.mobile') #想返回关联表的mobile字段
    class Meta:
        model = Account
        fields = ('username','password')

class ContactSerializers(serializers.ModelSerializer):

    # acc=serializers.CharField(source='account.username') #使返回的acc为account表里的username
    class Meta:
        model = Contact
        fields = '__all__' #包含上面的acc
