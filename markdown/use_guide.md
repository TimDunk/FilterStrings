#                                                         使用说明



### 什么时候使用?

>需要从字符串中提取多个符合指定规则的子字符串。例如存在这样的应用场景，当HTTP POST请求多达数十上百个，想从每一个请求中提取出传参用于对压力测试/性能测试的脚本进行参数化，若手工去操作，则会非常耗时且容易出错。
>



### 准备工具

- Chrome或其他浏览器

- 按照python程序httpRunner 3.0以上版本

- 当前extractToFile.exe程序

  

### 获取Http请求数据

>   1、先导出接口请求的HAR文件，HAR文件可以通过浏览器自带的Chome DevTools、Charles和Fiddler工具导出：
>  
>*Chome DevTools：*  
>   
>   ![avatar](.\markDownPic\pic5.png)  

 >  2、HAR文件转为py文件可以使用httpRunner 3.0版本的命令
 ```shell
 har2case har/postman-echo-post-form.har
 ```
 >也可以转为json文件  
 ```shell
 har2case -2j har/postman-echo-post-form.har
 ```
  >也可以转为yaml文件  
 ```shell
 har2case -2y har/postman-echo-post-form.har
 ```



### 提取内容到文件

> 1、准备一份需要从中提取子字符串的文件，例如
getCategoryAndCloudMaterialListWithOutContent_test.py文件记录的是HTTP请求的数据，其中with_data后面圆括号内的是请求的参数
![avatar](.\markDownPic\pic1.png)

  

> 2、从多个这个接口请求记录中提取Category与SubApp的值输出到文件，网上提供的正则表达式测试小程序可以验证到可以用正则表达式`with_data\(\{.*,"Category":\s*"(\d+)",.*"SubApp":\s*"(.*?)",`  
> 进行内容提取

 


> 3、打开本程序的默认配置文件或自己指定一个配置文件，编写如下配置:  
>   其中分号开头和#号开头的行是注释。  
>   [DEFAULT] 是默认配置，如果程序读取的值在后文没有配置相应的键值对，程序会从[DEFAULT]下读取。  
>   Expression 的值填写的是正则表达式  
>   FileSuffix 的值是输出文件的后缀名
>   Delimeter 的值是输出内容的每一行内容的分隔符
```ini
[DEFAULT]
Delimeter=,
;输出文件的格式后缀,在没有指定输出文件的时候生效
FileSuffix=.txt

[RegExp]
;此处填入正则表达式，注意是合法的正则表达书
; Expression = with_data\({.*,"Category":\s*"(\d+)",.*
; Expression="with_data\(\{.+\"materialId\":\"(.+)\"\}'\}\)"
; Expression="with_json\(\{\"materialIds\":\s*\"(.+)\"\s*\}\)"  #getDesignMaterialByIdsWithOutPlaceheights
; Expression="with_data\(\{.*,\"categoryId\":\s*\"(\d+)\",.*"  #getDesignMaterialListByCategoryIdExByEs      #getDesignmaterialListByCategoryIdWithRelationByEs
; Expression="with_data\(\{.*,\"Category\":\s*\"(\d+)\",.*"
Expression=with_data\(\{.*,"Category":\s*"(\d+)",.*"SubApp":\s*"(.*?)",

[Output]
;输出文件中的分割符号，默认是逗号;制表符是 \t
;Delimeter= \t
```
>   4、配置文件和要提取的Http请求参数的文件准备好后，使用cmd或Powershell输入如下命令，可完成数据的提取：  
```shell
PS D:\extractToFile> .\extractToFile.exe -s D:\PythonProjects\FilterStrings\getCategoryAndCloudMaterialListWithOutContent_test.py
```

>![avatar](.\markDownPic\pic3.png)  
>
>这个extractToFile.exe是一个命令行程序，使用方法可以查看帮助信息:  
![avatar](.\markDownPic\pic2.png)



### 后续流程

>   获得所需内容的文件后，这个文件可以用于Jmeter脚本的参数化文件。

