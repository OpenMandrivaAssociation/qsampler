Name:          qsampler
Summary:       LinuxSampler GUI front-end application
Version:       0.2.2
Release:       %mkrel 1
License:       GPL
Group:	       Sound
Source0:       %{name}-%{version}.tar.gz
URL: 	       http://qsampler.sourceforge.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: liblscp-devel
BuildRequires: qt4-devel
BuildRequires: libgig-devel
Requires:      linuxsampler

%description
QSampler is a LinuxSampler GUI front-end application written in 
C++ around the Qt4 toolkit using Qt Designer. At the moment it 
just wraps as a client reference interface for the LinuxSampler 
Control Protocol (LSCP).

%files
%defattr(-,root,root)
%{_bindir}/qsampler
%{_datadir}/applications/qsampler.desktop
%{_datadir}/pixmaps/qsampler.png
%{_datadir}/locale/*.qm

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-%version

%build
%configure2_5x
%make

%install
#make DESTDIR=%buildroot  install
%makeinstall

%clean
rm -fr %buildroot

