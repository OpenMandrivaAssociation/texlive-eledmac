Name:		texlive-eledmac
Version:	45418
Release:	1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eledmac
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledmac.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/eledmac
%doc %{_texmfdistdir}/doc/latex/eledmac
#- source
%doc %{_texmfdistdir}/source/latex/eledmac

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
