from kazoo.client import KazooClient


def get_cannal_instance_status(instance_id):
    zk = KazooClient(hosts='172.26.123.234:2181')
    zk.start()
    tmp_znode = zk.get_children(f"/otter/canal/destinations/{instance_id}")
    if "running" in tmp_znode:
        instance_context = zk.get(f"/otter/canal/destinations/{instance_id}/running")
        instance_status = instance_context
        print(instance_id, instance_status)
    zk.stop()


instance_id='rm-2ze4e6z5o42k086a4.P'
get_cannal_instance_status(instance_id)