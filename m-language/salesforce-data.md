---
title: "Salesforce.Data | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0c44b4a1-76d9-46cf-94bc-b067526945f0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Salesforce.Data
<code>Salesforce.Data(optional **loginUrl** as any, optional **options** as nullable record) as table</code>

## About

Returns the objects on the Salesforce account provided in the credentials. The account will be connected through the provided environment <code>loginUrl</code>. If no environment is provided then the account will connect to production (https://login.salesforce.com). An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 
* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).
* <code>ApiVersion</code> : The Salesforce API version to use for this query. When not specified, API version 29.0 is used. 
