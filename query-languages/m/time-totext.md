---
title: "Time.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.ToText

`Time.ToText(**time** as nullable time, optional **format** as nullable text, optional **culture** as nullable text) as nullable text`

## About
Returns a textual representation of `time`, the Time value, `time`. This function takes in an optional format parameter `format`. For a complete list of supported formats, please refer to the Library specification document.

## Example 1
Get a textual representation of #time(11, 56, 2).

``` 
Time.ToText(#time(11, 56, 2))
``` 


``` 
"11:56 AM"
``` 

## Example 2
Get a textual representation of #time(11, 56, 2) with format option.
``` 
Time.ToText(#time(11, 56, 2), "hh:mm")
``` 

``` 
"11:56"
```  
