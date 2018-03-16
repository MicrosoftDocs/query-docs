---
title: "SapHana.Database | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1168999d-39cc-45b2-be6d-a5e0190eb8d4
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SapHana.Database
<code>SapHana.Database(**server** as text, optional **options** as nullable record) as table</code>

## About
Returns a table of multidimensional packages from the SAP HANA database <code>server</code>. An optional record parameter, <code>options</code>, may be specified to control the following options: 
*  <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
*  <code>Distribution</code> : A SapHanaDistribution that sets the value of the &quot;Distribution&quot; property in the connection string. Statement routing is the method of evaluating the correct server node of a distributed system before statement execution. The default value is SapHanaDistribution.All.
  
