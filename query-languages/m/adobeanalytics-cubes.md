---
title: "AdobeAnalytics.Cubes | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AdobeAnalytics.Cubes


## Syntax

<pre>  
AdobeAnalytics.Cubes(optional <b>options</b> as nullable record) as table
</pre>

## About
Returns a table of multidimensional packages from Adobe Analyics. An optional record parameter, `options`, may be specified to control the following options: <ul> <li>`HierarchicalNavigation` : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).</li> <li>`MaxRetryCount` : The number of retries to perform when polling for the result of the query. The default value is 120.</li> <li>`RetryInterval` : The duration of time between retry attempts. The default value is 1 second.</li> </ul> 