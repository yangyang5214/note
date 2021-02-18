## kafka demo

### 启动

- 启动 zkServer 

  ```bash
  bash zkServer.sh ../conf/zoo.cfg 
  ```

- 启动 kafka

```bash
bash kafka-server-start.sh ../config/server.properties
```

- 创建 Topic

  直接运行 *kafka-topics.sh* 如果缺少参数会有提示

```bash
bash kafka-topics.sh --create --topic beer --zookeeper localhost:2181 --partitions 2 --replication-factor 1
```

- list

```bash
# 注意 __consumer_offsets 也是一个 topic
pi@raspberrypi:~/java/kafka_2.13-2.7.0$ bash bin/kafka-topics.sh --zookeeper localhost:2181 --list
OpenJDK Client VM warning: G1 GC is disabled in this release.
__consumer_offsets
beer
```

- desc

```bash
pi@raspberrypi:~/java/kafka_2.13-2.7.0$ bash bin/kafka-topics.sh --zookeeper localhost:2181 --describe --topic beer
OpenJDK Client VM warning: G1 GC is disabled in this release.
Topic: beer	PartitionCount: 2	ReplicationFactor: 1	Configs: 
	Topic: beer	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	Topic: beer	Partition: 1	Leader: 0	Replicas: 0	Isr: 0
```

- 测试

```bash
# consumer
bash bin/kafka-console-consumer.sh --bootstrap-server 192.168.31.158:9092  --topic beer
# producer
bash bin/kafka-console-producer.sh --broker-list  192.168.31.158:9092 --topic beer
```

### 代码

- producer

构造 KafkaProducer

```java
private final Logger logger = Logger.getLogger(KafkaProducer.class.getName());
@Bean
public KafkaProducer initKafkaProducer() {
    Properties properties = new Properties();
    properties.put("bootstrap.servers", "192.168.31.158:9092");
    properties.put("acks", "all");
    properties.put("retries", 3);
    properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
    properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
    return new KafkaProducer(properties);
}
```

send msg 

```java
public void send(KafkaProducer kafkaProducer, ProducerRecord producerRecord) {
    kafkaProducer.send(producerRecord, (metadata, exception) -> {
        if (exception != null) {
            logger.severe(exception.getMessage());
        }
    });
}
```

- Consumer

```java
Properties properties = new Properties();
properties.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
properties.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
properties.put("group.id", "test-consumer-group");
properties.put("enable.auto.commit", "true");
properties.put("bootstrap.servers", "192.168.31.158:9092");
KafkaConsumer kafkaConsumer =  new KafkaConsumer(properties);


kafkaConsumer.subscribe(Arrays.asList(topic));
int flag = 0;
while (flag < 5) {
    ConsumerRecords<String, String> consumerRecords = kafkaConsumer.poll(Duration.ofMillis(1000));
    Iterator<ConsumerRecord<String, String>> iterator = consumerRecords.iterator();
    while (iterator.hasNext()) {
        ConsumerRecord record = iterator.next();
        log.info("Kafka consumer: topic: {}, key:{}, value: {}", record.topic(), record.value(), record.key());
    }
    flag++;
}
```



