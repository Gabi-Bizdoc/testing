import abc

from testing import rpc_utils
from testing import config

class HelloBase(object):

    _QUEUE_NAME = 'hello'

    def __init__(self, host=None, username=None, password=None):
        host = host or config.host
        username = username or config.host
        password = password or config.password

        self._connection, self._channel = rpc_utils.create_connection(
            'localhost', 'stackrabbit', 'Passw0rd')
        self._channel.queue_declare(queue=self._QUEUE_NAME)

    def close(self):
        self._connection.close()

    @abc.abstractmethod
    def hello(self, foo, bar):
        pass


class HelloRPCAPI(HelloBase):

    def hello(self, foo, bar):
        self._publish('hi')

    def _publish(self, body):
        print(" [x] Sending '%r'" % body)
        self._channel.basic_publish(exchange='',
                                    routing_key=self._QUEUE_NAME,
                                    body=body)


class HelloRPCEndpoint(HelloBase):

    def hello(self, foo, bar):
        print "Heya! Got an RPC call..."
        print "foo='%(foo)s' bar='%(bar)s'" % dict(foo=foo, bar=bar)

    def _callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

    def start_consuming(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self._channel.basic_consume(self._callback,
                                    queue=self._QUEUE_NAME,
                                    no_ack=True)
        self._channel.start_consuming()