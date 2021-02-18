## kafka
### 术语

- Topic
- Producer
- Consumer
- Broker
- Replication
- Replica (Leader , Follower)
- Offset

### 参数

- log.dirs

```
逗号分隔的多个路径
```

- zookeeper.connect

```
zk 关联
```

- listeners
- auto.create.topics.enable
- log.retention.hours=168  默认七天

### 分区

主题 -> 分区  -> 消息

分区的作用就是提供负载均衡的能力。实现系统的高伸缩性。类似 es 的分片

分区策略

**决定生产者将消息发送到哪个分区的算法**

#### 轮询策略

默认

#### 随机策略

#### 自定义分区策略

#### 源码

评论区的一个例子（一个应用）

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/bed/20210216225756.png)

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/bed/20210216230743.png)

TODO

##### DefaultPartitioner

##### RoundRobinPartitioner

##### UniformStickyPartitioner

### 压缩

- Producer  压缩
- Consumer  解压
- Broker

### 消息丢失

- Producer

```
// callback and log error msg
public void send(KafkaProducer kafkaProducer, ProducerRecord producerRecord) {
    kafkaProducer.send(producerRecord, (metadata, exception) -> {
        if (exception != null) {
            logger.severe(exception.getMessage());
        }
    });
}
public void sendFire(KafkaProducer kafkaProducer, ProducerRecord producerRecord) {
    kafkaProducer.send(producerRecord);
}
```

- Consumer 

Ack 参数

```
  //ProducerConfig 

  public static final String ACKS_CONFIG = "acks";
    private static final String ACKS_DOC = "The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the "
                                           + " durability of records that are sent. The following settings are allowed: "
                                           + " <ul>"
                                           + " <li><code>acks=0</code> If set to zero then the producer will not wait for any acknowledgment from the"
                                           + " server at all. The record will be immediately added to the socket buffer and considered sent. No guarantee can be"
                                           + " made that the server has received the record in this case, and the <code>retries</code> configuration will not"
                                           + " take effect (as the client won't generally know of any failures). The offset given back for each record will"
                                           + " always be set to <code>-1</code>."
                                           + " <li><code>acks=1</code> This will mean the leader will write the record to its local log but will respond"
                                           + " without awaiting full acknowledgement from all followers. In this case should the leader fail immediately after"
                                           + " acknowledging the record but before the followers have replicated it then the record will be lost."
                                           + " <li><code>acks=all</code> This means the leader will wait for the full set of in-sync replicas to"
                                           + " acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica"
                                           + " remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting."
                                           + "</ul>";
```



#### acks

- 0 

  ```
  If set to zero then the producer will not wait for any acknowledgment from the server at all. The record will be immediately added to the socket buffer and considered sent
  ```

- 1 

```
This will mean the leader will write the record to its local log but will respond  without awaiting full acknowledgement from all followers
```

- All

```
This means the leader will wait for the full set of in-sync replicas to acknowledge the record.
```

### 消息交付

消息交付的三种情况：

- 最对一次。消息可能休息，但不会重复发送
- 至少一次。消息不会丢失，可能重复发送
- 精确一次。消息不会丢失，也不会重复发送



