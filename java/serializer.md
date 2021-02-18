## serializer

> 看到 Kafka 的 StringSerializer StringDeserializer ，复习一下 serializer

https://www.youtube.com/watch?v=6B6vp0jZnb0
https://developer.ibm.com/zh/articles/j-lo-serial/
https://www.tutorialspoint.com/java/java_serialization.htm

### what's  this

序列化

object to a sequence of bytes  对象转字节序列

### 例子

```java
package com.beer.learn.entity;

import java.io.*;

public class SerializerTest {


    public static void main(String[] args) {
        Order order = new Order();
        order.setId("00001");
        order.setName("beer");


        //save file
        try {
            FileOutputStream outputStream = new FileOutputStream("order.ser");
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
            objectOutputStream.writeObject(order);
            objectOutputStream.close();
            outputStream.close();
        } catch (Exception e) {
        }


        Order orderRead = null;
        try {
            FileInputStream fileIn = new FileInputStream("order.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);
            orderRead= (Order) in.readObject();
            in.close();
            fileIn.close();
        } catch (Exception i) {
        }
        System.out.println(orderRead);
    }
}

//Order
package com.beer.learn.entity;

import lombok.Data;

import java.io.Serializable;

@Data
public class Order implements Serializable {

    private String name;
    private String id;
}

```

### reason

- 跨 JVM 沟通。分布式应用（kafka）

- 持久化

- 补充

#### ![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/bed/20210218222208.png)



### ⚠️

#### 序列化 ID

验证版本一致？（序列化后的文件泄漏，数据也不会泄漏？）
下列是测试报错

```java
java.io.InvalidClassException: com.beer.learn.entity.Order; local class incompatible: stream classdesc serialVersionUID = 6103925441958716133, local class serialVersionUID = 1
	at java.base/java.io.ObjectStreamClass.initNonProxy(ObjectStreamClass.java:724)
	at java.base/java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:2045)
	at java.base/java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1895)
	at java.base/java.io.ObjectInputStream.readOrdinaryObject(ObjectInputStream.java:2202)
	at java.base/java.io.ObjectInputStream.readObject0(ObjectInputStream.java:1712)
	at java.base/java.io.ObjectInputStream.readObject(ObjectInputStream.java:519)
	at java.base/java.io.ObjectInputStream.readObject(ObjectInputStream.java:477)
	at com.beer.learn.entity.SerializerTest.main(SerializerTest.java:29)
```

#### 静态变量

序列化的是对象，静态变量属于类对象，没影响。（网上很多的测试用例感觉都有问题。。。）

#### Transient 

不序列化

*HashMap* 一些属性被 Transient 修饰

https://stackoverflow.com/questions/9144472/why-is-the-hash-table-of-hashmap-marked-as-transient-although-the-class-is-seria

#### writeObject readObject

用户自定义序列化过程

还是 *HashMap* 应用 （See in HashMap）



