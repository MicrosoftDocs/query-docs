---
description: "Learn more about: SapHana.Database"
title: "SapHana.Database | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# SapHana.Database

## Syntax

<pre>
SapHana.Database(**server** as text, optional **options** as nullable record) as table
</pre>

## About
Returns a table of multidimensional packages from the SAP HANA database `server`. An optional record parameter, `options`, may be specified to control the following options: 
*  `Query` : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
*  `Distribution` : A SapHanaDistribution that sets the value of the &quot;Distribution&quot; property in the connection string. Statement routing is the method of evaluating the correct server node of a distributed system before statement execution. The default value is SapHanaDistribution.All.
  
