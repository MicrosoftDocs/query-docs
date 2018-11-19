---
title: "ActiveDirectory.Domains | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ActiveDirectory.Domains

## Syntax

<pre>  
ActiveDirectory.Domains(optional <b>forestRootDomainName</b> as nullable text) as table
</pre>
  
## About

Returns a list of Active Directory domains in the same forest as the specified domain or of the current machine's domain if none is specified.