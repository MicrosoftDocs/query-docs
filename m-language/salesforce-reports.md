---
title: "Salesforce.Reports | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a9b93b1a-6ed8-475d-a8ea-ca137f42f058
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Salesforce.Reports
<code>Salesforce.Reports(optional **loginUrl** as nullable text, optional **options** as nullable record) as table</code>

## About

Returns the reports on the Salesforce account provided in the credentials. The account will be connected through the provided environment <code>loginUrl</code>. If no environment is provided then the account will connect to production (https://login.salesforce.com). An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: <code>ApiVersion</code> : The Salesforce API version to use for this query. When not specified, API version 29.0 is used.

