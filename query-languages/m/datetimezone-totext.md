---
title: "DateTimeZone.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.ToText
<code>DateTimeZone.ToText(**dateTimeZone** as nullable datetimezone, optional **format** as nullable text, optional **culture** as nullable text) as nullable text</code>
  
## About  
Returns a textual representation of <code>dateTimeZone</code>, the datetimezone value, <code>dateTimeZone</code>. This function takes in an optional format parameter <code>format</code>. For a complete list of supported formats, please refer to the Library specification document.
  
## Example 1
Get a textual representation of #datetimezone(2011, 12, 31, 11, 56, 2, 8, 0).

```
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 8, 0))
```

```
"12/31/2010 11:56:02 AM +08:00"
```


## Example 2
Get a textual representation of #datetimezone(2010, 12, 31, 11, 56, 2, 10, 12) with format option.


```
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 10, 12), "yyyy/MM/ddThh:mm:sszzz")
```

```
"2010/12/31T11:56:02+10:12"
```
