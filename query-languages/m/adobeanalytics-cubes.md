---
title: "AdobeAnalytics.Cubes | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AdobeAnalytics.Cubes
<code>AdobeAnalytics.Cubes(optional <b>options</b> as nullable record) as table</code>

## About

Returns a table of multidimensional packages from Adobe Analyics. An optional record parameter, `options`, may be specified to control the following options: 

- `MaxRetryCount`: The number of retries to perform when polling for the result of the query. The default value is 120.
 - `RetryInterval`: The duration of time between retry attempts. The default value is 1 second. 