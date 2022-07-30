---
description: "Learn more about: HdInsight.Contents"
title: "HdInsight.Contents"
ms.date: 7/29/2019
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# HdInsight.Contents

## Syntax

<pre>
HdInsight.Contents(<b>account</b> as text) as table
</pre>
  
## About  
Returns a navigational table containing a row for each container found at the account URL, `account`, from an Azure storage vault. Each row contains a link to the container blobs.
