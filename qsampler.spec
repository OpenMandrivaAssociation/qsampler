Name:          qsampler
Summary:       LinuxSampler GUI front-end application
Version:       0.2.1
Release:       %mkrel 2
License:       GPL
Group:	       Sound
Source0:       %{name}-%{version}.tar.gz
URL: 	       http://qsampler.sourceforge.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: liblscp-devel
BuildRequires: qt4-devel

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

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-%version

%build
%configure


make

%install
make DESTDIR=%buildroot  install

%clean
rm -fr %buildroot

