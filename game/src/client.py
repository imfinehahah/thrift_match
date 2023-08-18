from match_client.match import Match  ## match.thrift 里实现的Service服务 Match
from match_client.match.ttypes import User ## match.thrift 里定义的struct结构User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from sys import stdin


from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


from sys import stdin

 # 将原来的通信 main 函数改写成operate函数，每次需要的时候调用一次建立通信传递信息
 # 目的是可以一直不断处理信息
 # 然后重写 main 函数，使之能不断从终端读入信息
def operate(op, user_id, user_name, score):
    # ...........................
    transport = TSocket.TSocket('127.0.0.1', 9090) # 客户端需要修改成服务端所在的IP地址

    # Buffering is critical. Raw sockets are very slow
    # 增加缓存区，提高socket速度
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    # 创建协议
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    # 创建客户端
    client = Match.Client(protocol) # 从模板上粘贴下来时记得要修改客户端的名字，这里是Match

    # Connect!
    # 启动客户端
    transport.open()


    # 针对 op 参数，分别进行 "增加" 与 "删出" 操作
    user = User(user_id, user_name, score)

    if op == "add":
        client.add_user(user, "")
    else:
        client.remove_user(user, "")

    transport.close()

    # ...........................

def main():
    for line in stdin:
        op, user_id, user_name, score = line.split(' ')
        operate(op, int(user_id), user_name, int(score))

 # 调用 main 函数
if __name__ == "__main__":
    main()
