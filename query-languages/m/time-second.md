---
title: "Time.Second | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Second

  
## About  
Returns the second component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

  
  
## Example  

Find the second value from a datetime value.

```powerquery-m
Time.Second(#datetime(2011, 12, 31, 9, 15, 36.5))
```

`36.5`
