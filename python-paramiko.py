import paramiko

# pip3 install pycrypto
# pip3 install paramiko
# https://www.cnblogs.com/lzc978/p/10978688.html

# 1.基于密码
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='c1.salt.com', port=22, username='GSuser', password='123')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()

# 2.基于密钥
private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', key=private_key)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()

# 3.上传执行命令方法


class SSHConnection(object):

    def __init__(self, host='192.168.12.68', port=22, username='locojoy',pwd='123321QQ!'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()  # 连接远程服务器
        self.upload('db.py','/tmp/1.py')  # 将本地的db.py文件上传到远端服务器的/tmp/目录下并改名为1.py
        self.cmd('df')  # 执行df 命令
        self.close()    # 关闭连接

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self,local_path,target_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path,target_path)

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        print(result)
        return result


obj = SSHConnection()
obj.run()
