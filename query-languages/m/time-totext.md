---
title: "Time.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 05b508ad-096e-42f6-9c1d-a9a9e862e309
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
