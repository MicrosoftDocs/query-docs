---
title: "Uri.BuildQueryString | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Uri.BuildQueryString
<code>Uri.BuildQueryString(**query** as record) as text</code>
## About
Assemble the record <code>query</code> into a URI query string, escaping characters as necessary.

## Example 
Encode a query string which contains some special characters.

<code>Uri.BuildQueryString([a="1", b="+$"])</code>

<code>"a=1&b=%2B%24"</code>

