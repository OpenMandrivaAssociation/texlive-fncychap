Name:		texlive-fncychap
Version:	20710
Release:	2
Summary:	Seven predefined chapter heading styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fncychap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Each style can be modified using a set of simple commands.
Optionally one can modify the formatting routines in order to
create additional chapter headings. This package was previously
known as FancyChapter.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fncychap/fncychap.sty
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjarne.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjarnes.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjornstrup.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/BjornstrupS.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Conny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Connys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Glenn.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Glenns.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Lenny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Lennys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/README
%doc %{_texmfdistdir}/doc/latex/fncychap/Rejne.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Rejnes.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Sonny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Sonnys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/fncychap.pdf
%doc %{_texmfdistdir}/doc/latex/fncychap/fncychap.tex
%doc %{_texmfdistdir}/doc/latex/fncychap/manifest.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
