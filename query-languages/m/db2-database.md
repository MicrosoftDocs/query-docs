---
title: "DB2.Database | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DB2.Database

## Syntax

<pre>
DB2.Database(**server** as text, **database** as text, optional **options** as nullable record) as table
</pre>

## About

Returns a table of SQL tables and views available in a DB2 database on server `server` in the database instance named `database`. The port may be optionally specified with the server, separated by a colon. An optional record parameter, `options`, may be specified to control the following options: 

*	`CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).

*	`NavigationPropertyNameGenerator` : A function that is used for the creation of names for navigation properties.

*	`Query` : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.

*	`CommandTimeout` : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.

*	`ConnectionTimeout` : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.

*	`HierarchicalNavigation` : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

*	`Implementation` : Specifies the internal database provider implementation to use. Valid values are: &quot;IBM&quot; and &quot;Microsoft&quot;.

*	`BinaryCodePage` : A number for the CCSID (Coded Character Set Identifier) to decode DB2 FOR BIT binary data into character strings. Applies to Implementation = &quot;Microsoft&quot;. Set 0 to disable conversion (default). Set 1 to convert based on database encoding. Set other CCSID number to convert to application encoding.

*	`PackageCollection` : Specifies a string value for package collection (default is &quot;NULLID&quot;) to enable use of shared packages required to process SQL statements. Applies to Implementation = &quot;Microsoft&quot;.

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example. 



