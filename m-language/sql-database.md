---
title: "Sql.Database | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0f52288a-adfb-473b-a52c-a88a733f823c
caps.latest.revision: 12
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Sql.Database
<code>Sql.Database(**server** as text, **database** as text, optional **options** as nullable record) as table</code>

## About


Returns a table of SQL tables, views, and stored functions from the SQL Server database <code>database</code> on server <code>server</code>. The port may be optionally specified with the server, separated by a colon or a comma. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.

* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
	
* <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.
	
* <code>MaxDegreeOfParallelism</code> : A number that sets the value of the &quot;maxdop&quot; query clause in the generated SQL query.
	
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
	
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent. 
	
* <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false). 
	
* <code>MultiSubnetFailover</code> : A logical (true/false) that sets the value of the &quot;MultiSubnetFailover&quot; property in the connection string (default is false).
	
* <code>UnsafeTypeConversions</code>
		
	

The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example. 
