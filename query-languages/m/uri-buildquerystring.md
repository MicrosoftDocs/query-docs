---
title: "Uri.BuildQueryString | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e1c3a27f-32fb-4bb5-abe7-c6726ee5e3a7
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Uri.BuildQueryString
<code>Uri.BuildQueryString(**query** as record) as text</code>
## About
Assemble the record <code>query</code> into a URI query string, escaping characters as necessary.

## Example 
Encode a query string which contains some special characters.

<code>Uri.BuildQueryString([a="1", b="+$"])</code>

<code>"a=1&b=%2B%24"</code>

