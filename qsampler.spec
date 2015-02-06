%define debug_package %{nil}

Name:          qsampler
Summary:       LinuxSampler GUI front-end application
Version:       0.2.2
Release:       2
License:       GPLv2
Group:         Sound
Source0:       %{name}-%{version}.tar.gz
URL:           http://qsampler.sourceforge.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: liblscp-devel
BuildRequires: qt4-devel
BuildRequires: libgig-devel
BuildRequires: desktop-file-utils

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
%setup -q -n %name-%version

%build
export CXXFLAGS="%{optflags}"
%configure
perl -pi -e "s/-llscp/-llscp -lX11/g" qsampler.pro
%make

%install
%makeinstall_std
# Fix the .desktop file by removing
# 2 non-Mdv key and 2 non-standard categories
desktop-file-install \
    --remove-key="X-SuSE-translate" \
    --remove-key="Version" \
    --remove-category="MIDI" \
    --remove-category="ALSA" \
    --remove-category="JACK" \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Aug 28 2009 Emmanuel Andry <eandry@mandriva.org> 0.2.2-1mdv2010.0
+ Revision: 421792
- New version 0.2.2

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-5mdv2009.0
+ Revision: 259976
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-4mdv2009.0
+ Revision: 247782
- rebuild

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add linuxsampler as require

* Sun Dec 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 120470
- import qsampler


