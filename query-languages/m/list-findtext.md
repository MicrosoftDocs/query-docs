---
title: "List.FindText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 31b0ac6c-0f0c-4d74-ba0c-39a214d3e7b6
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
