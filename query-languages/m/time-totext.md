---
title: "Time.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.ToText

<code>Time.ToText(**time** as nullable time, optional **format** as nullable text, optional **culture** as nullable text) as nullable text</code>

## About
Returns a textual representation of <code>time</code>, the Time value, <code>time</code>. This function takes in an optional format parameter <code>format</code>. For a complete list of supported formats, please refer to the Library specification document.

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
