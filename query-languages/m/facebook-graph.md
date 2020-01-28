---
title: "Facebook.Graph | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Facebook.Graph

>[!Important]
>
>**Deprecation of Facebook data connector notice**
>
>Import and refresh data from Facebook in Excel will stop working in April, 2020. You will still be able to use the Facebook Get & Transform (Power Query) connector until then, but starting in April, 2020, you will be unable to connect to Facebook and will receive an error message. We recommend revising or removing any existing Get & Transform (Power Query) queries that use the Facebook connector as soon as possible to avoid unexpected results.

## Syntax

<pre>
Facebook.Graph(<b>url</b> as text) as any  
</pre>
  
## About  
Returns a record containing a set of tables found in the Facebook graph at the specified URL, `url`.

  