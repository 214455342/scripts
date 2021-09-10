from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

credentials = AccessKeyCredential('LTAI5tGD5HFgCGaMMxvL5oRD', 'G56NOrfS8UhTO8cFpPjIgFMZMKhcEf')
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>');
client = AcsClient(region_id='cn-beijing', credential=credentials)

request = DescribeInstancesRequest()
request.set_accept_format('json')
# request.set_PageNumber(20)
# request.set_PageSize(1)
request.set_Filter1Key("i-2ze2algvue1ho8nad18z")
response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
