---
title: "DateTimeZone.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.ToText

## Syntax

<pre>
DateTimeZone.ToText(**dateTimeZone** as nullable datetimezone, optional **format** as nullable text, optional **culture** as nullable text) as nullable text
</pre>
  
## About  
Returns a textual representation of `dateTimeZone`, the datetimezone value, `dateTimeZone`. This function takes in an optional format parameter `format`. For a complete list of supported formats, please refer to the Library specification document.
  
## Example 1
Get a textual representation of #datetimezone(2011, 12, 31, 11, 56, 2, 8, 0).

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 8, 0))
```

```powerquery-m
"12/31/2010 11:56:02 AM +08:00"
```


## Example 2
Get a textual representation of #datetimezone(2010, 12, 31, 11, 56, 2, 10, 12) with format option.

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 10, 12), "yyyy/MM/ddThh:mm:sszzz")
```

```powerquery-m
"2010/12/31T11:56:02+10:12"
```
