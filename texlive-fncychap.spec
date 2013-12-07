# revision 20710
# category Package
# catalog-ctan /macros/latex/contrib/fncychap
# catalog-date 2010-12-10 10:22:28 +0100
# catalog-license lppl1.3
# catalog-version v1.34
Name:		texlive-fncychap
Version:	v1.34
Release:	3
Summary:	Seven predefined chapter heading styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fncychap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.34-2
+ Revision: 752001
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.34-1
+ Revision: 718471
- texlive-fncychap
- texlive-fncychap
- texlive-fncychap
- texlive-fncychap

