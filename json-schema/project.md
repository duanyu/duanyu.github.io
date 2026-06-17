## 基本功能

输入：一段json结构的示例，纯文本的格式

输出：提示词。一个用来生成json schema，一个用来生成pydantic类代码（选择生成哪个，取决于用户的选择）

提示词1：生成json schema
根据这个json结构，生成json schema（OpenAI json schema格式，无需description，additionalProperties需要用False而非false）：
{json_data}

提示词2：生成pydantic
根据这个json结构，生成pydantic V2的定义代码（无需description）：
{json_data}

## 界面设计

整体而言，页面分为上下结构。

上部分占80%，又分为左右结构。
左侧放输入（即文本格式的json示例），下方放两个按钮“-> Json Schema”、“-> Pydantic”
右侧放拼接后的prompt结果，并方便直接复制。

下部分占20%，主要放一些固定的、常用的、与使用json schema息息相关的代码片段：

代码片段1（openai client使用json schema）
```python
response_format = {
    'type': 'json_schema',
    'json_schema':{
        'name': 'json_schema',
        'schema': json_schema
    }
}
```

代码片段2（openai client使用pydantic V2）
```python
response_format = {
    'type': 'json_schema',
    'json_schema':{
        'name': 'json_schema',
        'schema': pydantic_class.model_json_schema()
    }
}

# 校验返回内容（resp）
from pydantic import ValidationError

try:
    pydantic_data = pydantic_class.model_validate_json(resp)
    json_data = pydantic_data.model_dump()
except ValidationError as e:
    print(e)
```

整个页面左上角放一个回到duanyu.github.io主页的按钮。


## 页面的风格

极简风、苹果产品风格。

## 数据统计

我想知道按钮被点击的次数，把这个放到页面的某个地方。
