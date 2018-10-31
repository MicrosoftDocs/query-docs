---
title: "Uri.BuildQueryString | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Uri.BuildQueryString
`Uri.BuildQueryString(**query** as record) as text`
## About
Assemble the record `query` into a URI query string, escaping characters as necessary.

## Example 
Encode a query string which contains some special characters.

`Uri.BuildQueryString([a="1", b="+$"])`

`"a=1&b=%2B%24"`

