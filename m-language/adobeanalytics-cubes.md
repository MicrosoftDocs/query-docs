---
title: "AdobeAnalytics.Cubes | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 75a1566c-f28e-4ad8-9292-c90e93884923
caps.latest.revision: 4
author: "MarkMcGeeAtAquent"
ms.author: "v-mamcge"
manager: "kfile"
---
# AdobeAnalytics.Cubes
<code>AdobeAnalytics.Cubes(optional <b>options</b> as nullable record) as table</code>

## About

Returns a table of multidimensional packages from Adobe Analyics. An optional record parameter, `options`, may be specified to control the following options: 

- `MaxRetryCount`: The number of retries to perform when polling for the result of the query. The default value is 120.
 - `RetryInterval`: The duration of time between retry attempts. The default value is 1 second. 