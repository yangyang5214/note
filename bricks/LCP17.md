## 速算机器人


直接写代码也没什么问题。。。

`评论区找到优秀的回答`

![](https://beer-1256523277.cos.ap-shanghai.myqcloud.com/blog/20210208145309.png)

### code


```python
def calculate(self, s):
    x, y = 1, 0
    for i in s:
        if i == "A":
            x = 2 * x + y
        if i == 'B':
            y = 2 * y + x
    return x + y 
```

```python
class Solution(object):
    def calculate(self, s):
        return 1 << len(s)
```