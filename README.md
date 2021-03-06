## My-Django-REST-Framework

&ensp;&ensp; Django REST framework 是用于构建 Web API(网络应用程序接口) 的强大而灵活的工具包，利用它我们可以自动生成符合 RESTful 规范的 API 、生成 Browserable 的交互页面以及非常细粒度的权限管理等。


### 项目目录树

 - 基础配置
 - 序列化
 - 请求和响应
 - 视图
 - 认证和权限
 - 视图集和路由
 - 模式和文档

### 效果图

 - API Root
![mydrf21][22]


 - API Schema
![mydrf22][23]


 - API Docs
![mydrf23][24]


### 使用步骤 

- 克隆版本库至本地
```
git@github.com:lichaoxiang/My-Django-REST-Framework.git
```

- 安装依赖文件
```
pip install -r requirements.txt
```

- 创建 MySQL 数据库

- 修改配置文件(password)

- 生成数据库
```
python manage.py makemigrations
python manage.py migrate
```


  [22]: http://p7kk8oo3f.bkt.clouddn.com/QQ20180829-225616@2x.png
  [23]: http://p7kk8oo3f.bkt.clouddn.com/QQ20180829-225918@2x.png
  [24]: http://p7kk8oo3f.bkt.clouddn.com/QQ20180829-230140@2x.png


### 参考文档
<a href="http://www.django-rest-framework.org/">http://www.django-rest-framework.org/</a>
