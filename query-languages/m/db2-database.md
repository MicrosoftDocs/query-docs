---
title: "DB2.Database | Microsoft Docs"
ms.date: 07/17/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DB2.Database

## Syntax

<pre>
DB2.Database(<b>server</b> as text, <b>database</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table of SQL tables and views available in a Db2 database on server <code>server</code> in the database instance named <code>database</code>. The port may be optionally specified with the server, separated by a colon. An optional record parameter, <code>options</code>, may be specified to control the following options: 

<ul> <li><code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).</li> <li><code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.</li> <li><code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.</li> <li><code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.</li> <li><code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.</li> <li><code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).</li> <li><code>Implementation</code> : Specifies the internal database provider implementation to use. Valid values are: &quot;IBM&quot; and &quot;Microsoft&quot;.</li> <li><code>BinaryCodePage</code> : A number for the CCSID (Coded Character Set Identifier) to decode Db2 FOR BIT binary data into character strings. Applies to Implementation = &quot;Microsoft&quot;. Set 0 to disable conversion (default). Set 1 to convert based on database encoding. Set other CCSID number to convert to application encoding.</li> <li><code>PackageCollection</code> : Specifies a string value for package collection (default is &quot;NULLID&quot;) to enable use of shared packages required to process SQL statements. Applies to Implementation = &quot;Microsoft&quot;.</li> <li><code>UseDb2ConnectGateway</code> : Specifies whether the connection is being made through a Db2 Connect gateway. Applies to Implementation = &quot;Microsoft&quot;.</li> </ul> The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example. 



