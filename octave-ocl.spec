%global octpkg ocl

Summary:	OpenCL support for GNU Octave
Name:		octave-ocl
Version:	1.2.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/ocl/
Source0:	https://downloads.sourceforge.net/octave/ocl-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.2.0
#BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(OpenCL)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%patchlist
octave-ocl-1.2.3-fix_specialize.patch
octave-ocl-1.2.3-add_missing_cassert.patch

%description
Package using OpenCL for parallelization of (SIMD) computations,
selectively using available OpenCL hardware.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

