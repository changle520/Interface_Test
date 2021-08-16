Yaml语法知识:
一:认识 YAML
　　YAML是一个类似 XML、JSON 的标记性语言。YAML 强调以数据为中心，并不是以标识语言为重点。因而 YAML 本身的定义比较简单，号称“一种人性化的数据格式语言”。
二：YAML 组织结构
    YAML 文件可以由一或多个文档组成（也即相对独立的组织结构组成），
    文档间使用“---”（三个横线）在每文档开始作为分隔符。同时，文档也可以使用“...”（三个点号）作为结束符（可选）
三：YAML 编写规范
   1、使用“#”来表示注释内容
   2、使用空格进行缩进
   3、序列表示
      使用“-”（横线） + 单个空格表示单个列表项
        例如：
            --- # 文档开始
            - 第一章 简介
      使用"[]"表示一组数据
        例如：
            --- # 文档开始
            [blue, red, green]
      组合表示。每个结构都可以嵌套组成复杂的表示结构
        例如：
            --- # 文档开始
            - [blue, red, green]     # 列表项本身也是一个列表
            - [Age, Bag]
            - site: {osc:www.oschina.net, baidu: www.baidu.com}  # 这里是同 键值表 组合表示
   4、键值表
      使用 “:”（冒号） + 空格表示单个键值对
        # 客户订单
        date: 2015-02-01
        customer:
          - name: Jai
        items:
          - no: 1234         # 订单号
          - descript: cpu
          - price: ￥800.00
      使用"{}"表示一个键值表
        # 客户订单
        date: 2015-02-01
        customer:
          - name: Jai
        items: {no: 1234, descript: cpu, price: ￥800.00}
      "? " 问号+空格表示复杂的键。当键是一个列表或键值表时，就需要使用本符号来标记
         # 使用一个列表作为键
         ? [blue, reg, green]: Color
         # 等价于
         ? - blue
           - reg
           - gree
         : Color
      组合表示。每个结构都可以嵌套组成复杂的表示结构。
       Color:
        - blue
        - red
        - green
        # 相当于 (也是 JSON 的表示)
        {Color: [blue, red, green]}
   5、文本块
      使用 “|” 和文本内容缩进表示的块：保留块中已有的回车换行。相当于段落块
       yaml: |      # 注意 ":" 与 "|" 之间的空格
      使用 “>” 和文本内容缩进表示的块：将块中回车替换为空格，最终连接成一行
       yaml: >      # 注意 ":" 与 ">" 之间的空格，另外可以使用空行来分段落
      使用定界符“”（双引号）、‘’（单引号）或回车表示的块：最终表示成一行。
       yaml:     # 使用回车的多行，最终连接成一行。
   6、数据类型的约定
      对一些常用数据类型的表示格式进行了约定，包括:
         integer: 12345     # 整数标准形式
         octal: 0o34        # 八进制表示，第二个是字母 o
         hex: 0xFF          # 十六进制表示

         float: 1.23e+3     # 浮点数
         fixed: 13.67       # 固定小数
         minmin: -.inf      # 表示负无穷
         notNumber: .NaN    # 无效数字

         null:              # 空值
         boolean: [true, false] # 布尔值
         string: '12345'    # 字符串

         date: 2015-08-23   # 日期
         datetime: 2015-08-23T02:02:00.1z  # 日期时间
         iso8601: 2015-08-23t21:59:43.10-05:00  # iso8601 日期格式
         spaced: 2015-08-23 21:59:43.10 -5      # ?
      “!”（叹号）显式指示类型，或自定义类型标识。单叹号通常是自定义类型，双叹号是内置类型
          isString: !!str 2015-08-23     # 强调是字符串不是日期数据
          picture: !!binary |            # Base64  图片
          R0lGODlhDAAMAIQAAP//9/X
          17unp5WZmZgAAAOfn515eXv
          Pz7Y6OjuDg4J+fn5OTk6enp
          56enmleECcgggoBADs=
   7、锚点与引用，定义数据的复用
      第一步：使用 “&” 定义数据锚点（即要复制的数据）
      第二步：使用 “*” 引用上述锚点数据（即数据的复制目的地）
         ---
         hr:
           - Mark McGwire
           # Following node labeled SS
           - &SS Sammy Sosa            # 定义要复制的数据
         rbi:
           - *SS # Subsequent occurrence   这里是数据复制目标
           - Ken Griffey