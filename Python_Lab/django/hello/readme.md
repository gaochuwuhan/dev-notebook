## django drf练习

#   规范
-   django 工程名下（hello文件夹）下的core包是所有app共享的，例如logger、django_http

- 每个django 的app下 models/views/serializers有自己的   __init__.py文件，里面要导入当前所有中所有模块的所有 例如view的__init__.py：
    from .jsonview import *


-   每个模块的导入都是绝对路径：
    即 不要用 from ..models import xx,应该用绝对路径，绝对路径是相对于settings文件里的basedir的，也就是django工程（本项目为hello）目录下，即用 from baiapp.models import xx

- url 
    url路径为 127.0.0.1:8008/app名/drf/xx_具体模型

