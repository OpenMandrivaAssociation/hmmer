Summary:	Profile HMMs for protein sequence analysis
Name:		hmmer
Version:	3.0
Release:	5
License:	GPLv3+
Group:		Sciences/Biology
Url:		http://hmmer.janelia.org
Source0:	ftp://selab.janelia.org/pub/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch1:		%{name}-3.0.makefile.patch
Patch2:		hmmer-3.0-getopts.patch
BuildRequires:	openmpi
BuildRequires:	pkgconfig(ompi)

%description
Profile hidden Markov models (profile HMMs) can be used to do sensitive
database searching using statistical descriptions of a sequence family's
consensus. HMMER is a freely distributable implementation of profile HMM
software for protein sequence analysis.

%files
%doc README INSTALL LICENSE RELEASE-NOTES Userguide.pdf
%doc documentation tutorial
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1
%patch2 -p1

%build
%configure2_5x --enable-mpi
%make

%check
%make check

%install
%makeinstall_std

