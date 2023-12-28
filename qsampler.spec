Name:		qsampler
Summary:	LinuxSampler GUI front-end application
Version:	0.9.11
Release:	1
License:	GPLv2
Group:		Sound/Midi
URL:		https://qsampler.sourceforge.io/
Source0:	https://sourceforge.net/projects/qsampler/files/qsampler/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(lscp)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(gig)
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)

Requires: linuxsampler

%description
QSampler is a LinuxSampler GUI front-end application written in
C++ around the Qt5 toolkit using Qt Designer. At the moment it
just wraps as a client reference interface for the LinuxSampler
Control Protocol (LSCP).

%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes

%make_build

%install
%make_install -C build

desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/org.rncbc.qsampler.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.qsampler.desktop
%{_datadir}/icons/hicolor/*x*/apps/org.rncbc.qsampler.png
%{_datadir}/icons/hicolor/*x*/mimetypes/org.rncbc.qsampler.application-x-qsampler-session.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.qsampler.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/org.rncbc.qsampler.application-x-qsampler-session.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/org.rncbc.qsampler.xml
%{_datadir}/metainfo/org.rncbc.qsampler.metainfo.xml
%{_mandir}/man1/*
%{_mandir}/*/man1/qsampler.1.*
