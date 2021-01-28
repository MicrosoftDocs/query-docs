---
description: "Learn more about: Table.Profile"
title: "Table.Profile | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.Profile

## Syntax

<pre>
Table.Profile(<b>table</b> as table, optional <b>additionalAggregates</b> as nullable list) as table
</pre>
  
## About  
<p>Returns a profile for the columns in <code>table</code>.</p> <p>The following information is returned for each column (when applicable): <ul> <li>minimum</li> <li>maximum</li> <li>average</li> <li>standard deviation</li> <li>count</li> <li>null count</li> <li>distinct count</li> </ul> </p>
