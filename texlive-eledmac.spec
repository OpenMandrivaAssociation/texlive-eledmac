# revision 32113
# category Package
# catalog-ctan /macros/latex/contrib/eledmac
# catalog-date 2013-11-09 07:49:01 +0100
# catalog-license lppl
# catalog-version 1.7.0
Name:		texlive-eledmac
Version:	1.7.0
Release:	4
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eledmac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for typesetting scholarly critical editions,
replacing the established ledmac package. Ledmac itself was a
LaTeX port of the plain TeX EDMAC macros. The package supports
indexing by page and by line numbers, and simple tabular- and
array-style environments. The package is distributed with the
related eledpar package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eledmac/eledmac.sty
%{_texmfdistdir}/tex/latex/eledmac/eledpar.sty
%doc %{_texmfdistdir}/doc/latex/eledmac/Makefile
%doc %{_texmfdistdir}/doc/latex/eledmac/README
%doc %{_texmfdistdir}/doc/latex/eledmac/eledmac.pdf
%doc %{_texmfdistdir}/doc/latex/eledmac/eledpar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eledmac/eledmac.dtx
%doc %{_texmfdistdir}/source/latex/eledmac/eledmac.ins
%doc %{_texmfdistdir}/source/latex/eledmac/eledpar.dtx
%doc %{_texmfdistdir}/source/latex/eledmac/eledpar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
