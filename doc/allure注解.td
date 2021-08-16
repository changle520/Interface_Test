注解使用：

一：功能模块方面的特性：
1）feature（主要功能模块--一级标签）
使用方法：@allure.feature()
2）story（子功能模块--二级标签）
使用方法：@allure.story()


二：测试用例方面的特性
1）title（用例标题）
使用方法：@allure.title
2）description（用例描述）
使用方法：@allure.description
3）step（测试用例步骤）
使用方法：@allure.step()


三：测试用例级别的特性：severity（BUG严重级别）
1）使用方法：@allure.severity(allure.severity_level.CRITICAL)
或者 @allure.severity('critical')

2）相关说明：　Allure中对严重级别的定义：

blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）

critical级别：临界缺陷（ 功能点缺失）

normal级别：普通缺陷（数值计算错误）

minor级别：次要缺陷（界面错误与UI需求不符）

trivial级别：轻微缺陷（必输项无提示，或者提示不规范）



四：链接方面的特性：link/issue/testcase（链接）
使用方法：

@allure.link(url='http://www.baidu.com',name='link_url')

@allure.issue(url='http://www.baidu.com',name='issue_url') #bug链接

@allure.testcase(url='http://www.tapd.com',name='testcase_url')



五：附件信息方面的特性：attach（附件信息）
使用方法：@allure.attach(body, name, attachment_type, extension)

body - 要写入文件的原始内容

name - 包含文件名的字符串

attachment_type - 其中一个allure.attachment_type值

extension - 提供的将用作创建文件的扩展名
