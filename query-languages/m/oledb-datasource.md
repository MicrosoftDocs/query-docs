---
title: "OleDb.DataSource | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# OleDb.DataSource
<code>OleDb.DataSource(<b>connectionString</b> as any, optional <b>options</b> as nullable record) as table</code>
## About
Returns a table of SQL tables and views from the OLE DB data source specified by the connection string <code>connectionString</code>. <code>connectionString</code> can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 
*  <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
*  <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.
*  <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
*  <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is true).
*  <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
*  <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
*  <code>SqlCompatibleWindowsAuth</code> : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example.
  
