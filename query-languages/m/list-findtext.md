---
title: "List.FindText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.FindText

  
## About  
Searches a list of values, including record fields, for a text value.  
  
```  
List.FindText(list as list, text as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to search.|  
|text|The value to search for.|  
  
## Example  
  
```  
List.FindText(  
  
{  
  
    [field1 = "t1", field2 = "t2" ],  
  
    [field1 = "test1", field2 = "test2" ],  
  
    [field1 = "another test", field2 = 5 ],  
  
    [field1 = 1, field2 = 2 ]  
  
}, "test")  
  
equals  
  
{  
  
    [field1 = "test1", field2 = "test2" ],  
  
    [field1 = "another test", field2 = 5 ]  
  
}  
  
List.FindText(  
  
{  
  
    [ Field1 = "hello", Field2 = "world" ],  
  
    [ Field1 = "hello1", Field2 = "hello2" ],  
  
    [ Field1 = "another test", Field2 = 5 ],  
  
    [ Field1 = 1, Field2 = 2 ]  
  
}, "hello")  
  
equals  
  
{  
  
    [Field1="hello", Field2 = "world"],  
  
    [Field1 = "hello1", Field2 = "hello2"]  
  
}  
```  
