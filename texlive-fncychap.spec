%global tl_name fncychap
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.34
Release:	%{tl_revision}.1
Summary:	Seven predefined chapter heading styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fncychap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Each style can be modified using a set of simple commands. Optionally
one can modify the formatting routines in order to create additional
chapter headings. This package was previously known as FancyChapter.

