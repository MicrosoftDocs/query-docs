---
title: M Language Sections | Microsoft Docs
description: Describes using sections in the Power Query M formula language
author: dougklopfenstein

ms.service: powerquery

ms.topic: article
ms.date: 4/7/2020
ms.author: bezhan
---

# Sections

A _section-document_ is an M program that consists of multiple named expressions.

_section-document:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section<br/>
section:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-attributes<sub>opt</sub>_  `section`  _section-name_  `;`  _section-members<sub>opt</sub><br/> 
section-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
section-members:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section-member section-members<sub>opt</sub><br/>
section-member:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-attributes<sub>opt</sub>_  `shared`_<sub>opt</sub> section-member-name_  `=`  _expression_  `;`<br/>
_section-member-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_

In M, a section is an organizational concept that allows related expressions to be named and grouped within a document. Each section has a _section-name_, which identifies the section and qualifies the names of the _section-members_ declared within the section. A _sectionmember_ consists of a _member-name_ and an _expression_. Section member expressions may refer to other section members within the same section directly by member name.

The following example shows a section-document that contains one section:

```
section Section1; 

A = 1;                          //1     
B = 2;                          //2 
C = A + B;                      //3
```

Section member expressions may refer to section members located in other sections by means of a _section-access-expression_, which qualifies a section member name with the name of the containing section.

_section-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_ `!` _identifier_

The following example shows a document containing two sections that are mutually referential:

```
section Section1; 
A = "Hello";                    //"Hello" 
B = 1 + Section2!A;             //3

section Section2; 
A = 2;                          //2 
B = Section1!A & " world!";     /"Hello, world"
```

Section members may optionally be declared as `shared`, which omits the requirement to use a _section-access-expression_ when referring to shared members outside of the containing section. Shared members in external sections may be referred to by their unqualified member name so long as no member of the same name is declared in the referring section and no other section has a like-named shared member.

The following example illustrates the behavior of shared members when used across sections within the same document:

```
section Section1;  
shared A = 1;        // 1 

section Section2; 
B = A + 2;           // 3 (refers to shared A from Section1) 

section Section3; 
A = "Hello";         // "Hello" 
B = A + " world";    // "Hello world" (refers to local A) 
C = Section1!A + 2;  // 3
```

Defining a shared member with the same name in different sections will produce a valid global environment, however accessing the shared member will raise an error when accessed.

```
section Section1; 
shared A = 1; 

section Section2; 
shared A = "Hello"; 
 
section Section3; 
B = A;    //Error: shared member A has multiple definitions
```

The following holds when evaluating a section-document:

* Each _section-name_ must be unique in the global environment.

* Within a section, each _section-member_ must have a unique _section-member-name_.

* Shared section members with more than one definition raise an error when the shared member is accessed.

* The expression component of a _section-member_ must not be evaluated before the section member is accessed.

* Errors raised while the expression component of a _section-member_ is evaluated are associated with that section member before propagating outward and then re-raised each time the section member is accessed.

## Document Linking

A set of M section documents can be linked into an opaque record value that has one field per shared member of the section documents. If shared members have ambiguous names, an error is raised.

The resulting record value fully closes over the global environment in which the link process was performed. Such records are, therefore, suitable components to compose M documents from other (linked) sets of M documents. There are no opportunities for naming conflicts.

The standard library functions `Embedded.Value` can be used to retrieve such "embedded" record values that correspond to reused M components.

## Document Introspection

M provides programmatic access to the global environment by means of the `#sections` and `#shared` keywords.

### #sections

The `#sections` intrinsic variable returns all sections within the global environment as a record. This record is keyed by section name and each value is a record representation of the corresponding section indexed by section member name.

The following example shows a document consisting of two sections and the record produced by evaluating the `#sections` intrinsic variable within the context of that document:

```
section Section1; 
A = 1; 
B = 2;  

section Section2;
C = "Hello"; 
D = "world"; 
 
#sections 
//[ 
//  Section1 = [ A = 1, B = 2], 
//  Section2 = [ C = "Hello", D = "world" ] 
//] 
```

The following holds when evaluating `#sections`:

* The `#sections` intrinsic variable preserves the evaluation state of all section member expressions within the document. 
* The `#sections` intrinsic variable does not force the evaluation of any unevaluated section members.

### #shared

The `#shared` intrinsic variable returns a record containing the names and values of all shared section members currently in scope.

The following example shows a document with two shared members and the corresponding record produced by evaluating the #shared intrinsic variable within the context of that document:

```
section Section1;
shared A = 1; 
B = 2; 
 
Section Section2;
C = "Hello";
shared D = "world"; 
 
//[ 
//  A = 1, 
//  D = "world" 
//] 
```

The following holds when evaluating `#shared`:

* The `#shared` intrinsic variable preserves the evaluation state of all shared member expressions within the document.

* The `#shared` intrinsic variable does not force the evaluation of any unevaluated section members.

