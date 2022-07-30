---
description: "Learn more about: AccessControlEntry.ConditionToIdentities"
title: "AccessControlEntry.ConditionToIdentities"
ms.date: 3/28/2019
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# AccessControlEntry.ConditionToIdentities

## Syntax

<pre>
AccessControlEntry.ConditionToIdentities(<b>identityProvider</b> as function, <b>condition</b> as function) as list
</pre>
  
## About  

<p>Using the specified <code>identityProvider</code>, converts the <code>condition</code> into the list of identities for which <code>condition</code> would return <code>true</code> in all authorization contexts with <code>identityProvider</code> as the identity provider. An error is raised if it is not possible to convert <code>condition</code> into a list of identities, for example if <code>condition</code> consults attributes other than user or group identities to make a decision.</p> <p>Note that the list of identities represents the identities as they appear in <code>condition</code> and no normalization (such as group expansion) is performed on them.</p> 

  
