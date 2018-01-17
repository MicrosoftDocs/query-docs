---
title: "AdoDotNet.DataSource | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
applies_to: 
  - "Power BI"
ms.assetid: 7eabb67c-8c42-4ba9-a38a-c89b70d5a084
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# AdoDotNet.DataSource
<code>AdoDotNet.DataSource(<b>providerName</b> as text, <b>connectionString</b> as any, optional <b>options</b> as nullable record) as table</code>

#### About
Returns the schema collection for the ADO.NET data source with provider name <code>providerName</code> and connection string <code>connectionString</code>. <code>connectionString</code> can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 
*  <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
*  <code>SqlCompatibleWindowsAuth</code> : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.

