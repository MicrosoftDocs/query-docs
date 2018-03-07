---
title: "AnalysisServices.Database | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 153ab044-1afc-4b1a-a64c-01c3c645717a
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# AnalysisServices.Database
<code>AnalysisServices.Database(**server** as text, **database** as text, optional **options **as nullable record) as table</code>

## About
Returns a table of multidimensional cubes or tabular models from the Analysis Services database <code>database</code> on server <code>server</code>. An optional record parameter, <code>options</code>, may be specified to control the following options: 



* <code>Query</code> : A native MDX query used to retrieve data.
* <code>TypedMeasureColumns</code> : A logical value indicating if the types specified in the multidimensional or tabular model will be used for the types of the added measure columns. When set to false, the type &quot;number&quot; will be used for all measure columns. The default value for this option is false.
* <code>Culture</code> : A culture name specifying the culture for the data. This corresponds to the &#39;Locale Identifier&#39; connection string property.
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is driver-dependent.
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
*  <code>SubQueries</code> : A number (0, 1 or 2) that sets the value of the &quot;SubQueries&quot; property in the connection string. This controls the behavior of calculated members on subselects or subcubes. (The default value is 2).
*  <code>Implementation</code>
  
