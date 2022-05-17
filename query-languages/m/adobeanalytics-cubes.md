---
description: "Learn more about: AdobeAnalytics.Cubes"
title: "AdobeAnalytics.Cubes | Microsoft Docs"
ms.date: 5/25/2021
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# AdobeAnalytics.Cubes

## Syntax

<pre>  
AdobeAnalytics.Cubes(optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table of multidimensional packages from Adobe Analyics. An optional record parameter, `options`, may be specified to control the following options:

* `HierarchicalNavigation`: A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).
* `MaxRetryCount`: The number of retries to perform when polling for the result of the query. The default value is 120.
* `RetryInterval`: The duration of time between retry attempts. The default value is 1 second.
* `Implementation`: Specifies the internal database provider implementation to use. Valid values are: "IBM" and "Microsoft".
