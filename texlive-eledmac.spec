%global tl_name eledmac
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.24.12
Release:	%{tl_revision}.1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eledmac
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for typesetting scholarly critical editions, replacing the
established ledmac package. Ledmac itself was a LaTeX port of the plain
TeX EDMAC macros. The package supports indexing by page and by line
numbers, and simple tabular- and array-style environments. The package
is distributed with the related eledpar package. The package is now
superseded by reledmac.

