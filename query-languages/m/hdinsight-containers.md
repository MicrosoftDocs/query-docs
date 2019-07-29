---
title: "HdInsight.Containers | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# HdInsight.Containers

## Syntax

<pre>
HdInsight.Containers(<b>account</b> as text) as table
</pre>
  
## About  
Returns a navigational table containing a row for each container found at the account URL, `account`, from an Azure storage vault. Each row contains a link to the container blobs.
